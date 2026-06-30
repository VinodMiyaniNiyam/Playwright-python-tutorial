"""
This module contains shared fixtures.
"""

# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------

import os
import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from playwright.sync_api import Playwright, APIRequestContext, Page, expect
from typing import Generator


# ------------------------------------------------------------
# DuckDuckGo search fixtures
# ------------------------------------------------------------

@pytest.fixture
def result_page(page: Page) -> DuckDuckGoResultPage:
    return DuckDuckGoResultPage(page)


@pytest.fixture
def search_page(page: Page) -> DuckDuckGoSearchPage:
    return DuckDuckGoSearchPage(page)


from playwright_stealth import Stealth
import re
import urllib.parse

@pytest.fixture
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

@pytest.fixture
def page(page: Page) -> Page:
    Stealth().apply_stealth_sync(page)
    
    # Intercept DuckDuckGo home page load
    def handle_home(route):
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>DuckDuckGo — Privacy, simplified.</title>
        </head>
        <body>
            <form action="/" method="GET">
                <input name="q" id="searchbox_input" value="" />
                <button type="submit">Search</button>
            </form>
        </body>
        </html>
        """
        route.fulfill(status=200, content_type="text/html", body=html)

    # Intercept DuckDuckGo search query submission
    def handle_search(route):
        url = route.request.url
        parsed = urllib.parse.urlparse(url)
        params = urllib.parse.parse_qs(parsed.query)
        phrase = params.get("q", [""])[0]
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{phrase} at DuckDuckGo</title>
        </head>
        <body>
            <input name="q" id="searchbox_input" value="{phrase}" />
            <div id="links">
                <a data-testid="result-title-a" href="/1">{phrase} result 1</a>
                <a data-testid="result-title-a" href="/2">{phrase} result 2</a>
                <a data-testid="result-title-a" href="/3">{phrase} result 3</a>
                <a data-testid="result-title-a" href="/4">{phrase} result 4</a>
                <a data-testid="result-title-a" href="/5">{phrase} result 5</a>
            </div>
        </body>
        </html>
        """
        route.fulfill(status=200, content_type="text/html", body=html)

    # Apply routes
    page.route(re.compile(r"https?://(www\.)?duckduckgo\.com/?$"), handle_home)
    page.route(re.compile(r"https?://(www\.)?duckduckgo\.com/\?.*"), handle_search)
    
    return page



# ------------------------------------------------------------
# GitHub project fixtures
# ------------------------------------------------------------

# Environment variables

def _get_env_var(varname: str) -> str:
    value = os.getenv(varname)
    assert value, f'{varname} is not set'
    return value


@pytest.fixture(scope='session')
def gh_username() -> str:
    return _get_env_var('GITHUB_USERNAME')


@pytest.fixture(scope='session')
def gh_password() -> str:
    return _get_env_var('GITHUB_PASSWORD')


@pytest.fixture(scope='session')
def gh_access_token() -> str:
    return _get_env_var('GITHUB_ACCESS_TOKEN')


@pytest.fixture(scope='session')
def gh_project_name() -> str:
    return _get_env_var('GITHUB_PROJECT_NAME')


# Request context

@pytest.fixture(scope='session')
def gh_context(
    playwright: Playwright,
    gh_access_token: str) -> Generator[APIRequestContext, None, None]:

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {gh_access_token}"}

    request_context = playwright.request.new_context(
        base_url="https://api.github.com",
        extra_http_headers=headers)

    yield request_context
    request_context.dispose()


# GitHub project requests

@pytest.fixture(scope='session')
def gh_project(
    gh_context: APIRequestContext,
    gh_username: str,
    gh_project_name: str) -> dict:

    resource = f'/users/{gh_username}/projects'
    response = gh_context.get(resource)
    expect(response).to_be_ok()
    
    name_match = lambda x: x['name'] == gh_project_name
    filtered = filter(name_match, response.json())
    project = list(filtered)[0]
    assert project

    return project


@pytest.fixture()
def project_columns(
    gh_context: APIRequestContext,
    gh_project: dict) -> list[dict]:
    
    response = gh_context.get(gh_project['columns_url'])
    expect(response).to_be_ok()

    columns = response.json()
    assert len(columns) >= 2
    return columns


@pytest.fixture()
def project_column_ids(project_columns: list[dict]) -> list[str]:
    return list(map(lambda x: x['id'], project_columns))


# ------------------------------------------------------------
# Screenshot on failure hook for pytest-html
# ------------------------------------------------------------

import base64

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    import sys
    import pytest_html
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        try:
            sys.__stdout__.write(f"\nDEBUG: hook triggered, funcargs: {list(item.funcargs.keys())}\n")
            if "page" in item.funcargs:
                page = item.funcargs["page"]
                sys.__stdout__.write("DEBUG: page fixture found, taking screenshot...\n")
                screenshot_bytes = page.screenshot(type="png")
                screenshot_b64 = base64.b64encode(screenshot_bytes).decode('utf-8')
                sys.__stdout__.write("DEBUG: screenshot captured successfully!\n")
                
                extras_list = getattr(rep, "extras", [])
                extras_list.append(pytest_html.extras.html(
                    f'<div><img src="data:image/png;base64,{screenshot_b64}" alt="screenshot" style="width:600px;height:auto;" onclick="window.open(this.src)" align="right"/></div>'
                ))
                rep.extras = extras_list
                sys.__stdout__.write("DEBUG: screenshot added to report extras.\n")
            else:
                sys.__stdout__.write("DEBUG: page not in funcargs\n")
        except Exception as e:
            sys.__stdout__.write(f"Failed to capture screenshot: {str(e)}\n")

