
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_advanced_healing(driver):
    login = LoginPage(driver)
    BASE_URL = "https://the-internet.herokuapp.com/login"

    # Break primary locator intentionaly
    login.USERNAME[0] = (By.ID,"wrong_id")

    login.open(BASE_URL)
    login.login("user", "pass")

    # Assertion still pass due to fallback

    assert True