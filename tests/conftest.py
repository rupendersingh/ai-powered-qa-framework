import logging
import sys
import os
import allure
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

    # Only act after test execution phase
    if rep.when == "call":
        driver = item.funcargs.get("driver", None)
        
        if driver is None:
            return
        
        test_name = item.name
         # -------------------------------
        # ALWAYS ATTACH SCREENSHOT
        # -------------------------------
        screenshot_path= f"reports/{test_name}.png"
        driver.save_screenshot(screenshot_path)

        with open(screenshot_path,"rb") as f:
            allure.attach(
                f.read(),
                name = "screenshot",
                attachment_type = allure.attachment_type.PNG
            )

            # -------------------------------
        # ATTACH HEAL LOG (IF EXISTS)
        # -------------------------------

        heal_log_path = "utils/heal_log.json"
        if os.path.exists(heal_log_path):
            with open(heal_log_path,"r") as f:
                allure.attach(
                    f.read(),
                    name= "self-Heal Log",
                    attachment_type=allure.attachment_type.JSON
                )
        # -------------------------------
        # ON FAILURE → AI ANALYSIS
        # -------------------------------

        if rep.failed:

            try:
                log_text = str(rep.longrepr)
                analysis = analyze(
                    screenshot_path = screenshot_path,
                    log_text=log_text,
                    page_title=driver.title
                )
                # Save failure report JSON
                failure_path = f"reports/{test_name}_failure.json"
                with open(failure_path, "w") as f:
                    json.dump(analysis,f,indent=2)

                #Attach to Allure
                allure.attach(
                    json.dump(analysis, indent=2),
                    name="AI Failure Analysis",
                    attachment_type= allure.attachment_type.JSON
                    )
            except Exception as e:
                # Fail-safe: do NOT break test reporting
                error_msg = f"AI analysis failed: {str(e)}"
                logging.error(error_msg)

                allure.attach(
                    error_msg,
                    name="AI Analysis Error",
                    attachment_type=allure.attachment_type.TEXT
                )