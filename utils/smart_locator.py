from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json, time, os

HEAL_LOG = "utils/heal_log.json"


def try_locators(driver, locators: list, timeout=10):

    for i, loc in enumerate(locators):
        try:
            element = WebDriverWait(driver, timeout // len(locators)).until(
                EC.presence_of_element_located(loc)
            )

            if i > 0:
                _log_heal(locators[0], loc)

            return element   # ✅ IMPORTANT — return WebElement

        except Exception:
            continue

    raise Exception("Element not found using any locator")


def _log_heal(primary, used):

    if os.path.exists(HEAL_LOG):
        with open(HEAL_LOG, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append({
        "primary": str(primary),
        "used": str(used),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    })

    with open(HEAL_LOG, "w") as f:
        json.dump(data, f, indent=2)