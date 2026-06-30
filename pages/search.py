"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from playwright.sync_api import Page


class DuckDuckGoSearchPage:

    URL = 'https://www.duckduckgo.com'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_button = page.locator('button[type="submit"]')
        self.search_input = page.locator('[name="q"]')
    
    def load(self) -> None:
        self.page.goto(self.URL)
    
    def search(self, phrase: str) -> None:
        self.search_input.fill(phrase)
        self.search_button.click()
