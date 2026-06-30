import os
import sys
import subprocess
from datetime import datetime

def main():
    # 1. Get current date and time
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H%M%S")
    
    # 2. Define the report path
    # e.g., reports/2026-06-30/run_122727/report.html
    report_dir = os.path.join("reports", date_str, f"run_{time_str}")
    os.makedirs(report_dir, exist_ok=True)
    report_file = os.path.join(report_dir, "report.html")
    
    # 3. Construct the pytest command
    # We target test_assignment.py (our assignment solutions) and test_search.py (web search)
    # We skip github tests since they require credentials, but they can be run if desired.
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/test_assignment.py",
        "tests/test_search.py",
        f"--html={report_file}",
        "--self-contained-html"
    ]
    
    print(f"Starting test execution...")
    print(f"Command: {' '.join(cmd)}")
    print(f"Report will be generated at: {os.path.abspath(report_file)}")
    
    # 4. Run pytest
    result = subprocess.run(cmd)
    
    print("\n" + "="*50)
    print(f"Execution finished with exit code: {result.returncode}")
    print(f"Standard report HTML: {os.path.abspath(report_file)}")
    print("="*50)
    
    # Return exit code
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
