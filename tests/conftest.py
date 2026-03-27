import sys
import os
import pytest
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from ai_modules.failure_analyzer import analyze
from pages.login_page import LoginPage

# Add project root to PYTHONPATH
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
  
    outcome = yield
    rep = outcome.get_result()
    print("HOOK:", rep.when, rep.failed)

    if rep.failed:
        driver = item.funcargs.get("driver",None)
        print("DRIVER:", driver)

        if driver:
            ts = time.strftime("%Y%m%d_%H%M%S")
            base = os.getcwd()
            folder = os.path.join(base, "reports", "failures", f"{item.name}__FAIL__{ts}")
            os.makedirs(folder,exist_ok=True)

            screenshot_path = os.path.join(folder, "screenshot.png")
            report_path = os.path.join(folder, "failure_report.json")

            # Screenshot
            driver.save_screenshot(screenshot_path)

            # Capture log (basic)
            log_text = str(rep.longrepr)

            try:
                analysis = analyze(log_text, driver.title)
            except Exception as e:
                analysis = {
                    "error_type": "Analyzer Failure",
                    "likely_cause": str(e),
                    "suggested_fix": "Check LLM response format",
                    "confidence": "Low"
                }

            print("ANALYSIS:", analysis)
            
            with open(report_path, "w") as f:
                json.dump(analysis, f, indent=2)
