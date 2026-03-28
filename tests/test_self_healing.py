
import os
print("RUNNING FILE:", __file__)

from selenium.webdriver.common.by import By

def test_self_healing(login_page):
    print("TEST VERSION 2")
    # Step 1 — Open page (THIS WAS MISSING)
    login_page.open("https://the-internet.herokuapp.com/login")
    print("URL OPEN CALLED")

    # Step 2 — Break primary locator intentionally
    login_page.USERNAME = [
        (By.CSS_SELECTOR, "#wrong-id"),
        (By.XPATH, "//input[@id='username']")
    ]

    # Step 3 — Perform login
    login_page.login("tomsmith", "SuperSecretPassword!")

    # Step 4 — Validate success message (BETTER than assert True)
    assert "secure area" in login_page.get_message().lower()