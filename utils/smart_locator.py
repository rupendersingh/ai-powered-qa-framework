from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json, time, os
from selenium.webdriver.common.by import By

HEAL_LOG = "utils/heal_log.json"


def try_locators(driver, locators: list, timeout=10):
    extended = []

    for loc in locators:
        extended.extend(build_extended_locators(loc,driver))

    for i, loc in enumerate(extended):
        try:
            element = WebDriverWait(driver, timeout // len(extended)).until(
                EC.presence_of_element_located(loc)
            )

            if i > 0:
                _log_heal(locators[0], loc)

            return element   # ✅ IMPORTANT — return WebElement

        except:
            print(f"FAILED locator {i}: {loc}")
            continue

    raise Exception(f"Element not found using extended healing strategy")


def _log_heal(primary, used):
    print("LOGGING HEAL EVENT")  # ADD THIS

    if os.path.exists(HEAL_LOG):
        with open(HEAL_LOG, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append({
        "primary": str(primary),
        "used": str(used),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "strategy": "fallback_chain",
        "confidence": "low"  # placeholder for future upgrade
    })

    with open(HEAL_LOG, "w") as f:
        json.dump(data, f, indent=2)

    
def build_extended_locators(primary_locator, driver):
    by, value = primary_locator
    extended = [primary_locator]

    #Existing fallback assumptions
    text_value = value if isinstance(value,str) else ""

    #Add semantic fallbacks

    extended +=[
        (By.XPATH, f"//*[@aria-label='{text_value}']"),
        (By.XPATH, f"//*[@placeholder='{text_value}']"),
        (By.NAME, text_value),
        (By.XPATH, f"//*[contains(text(),'{text_value}')]")
    ]

    return extended

def heal_rate():
    import json
    logs = json.load(open("utils/heal_log.json"))
    print(f"Total heals: {len(logs)}")
