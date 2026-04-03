import pytest
import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.visual_utils import VisualValidator

BASE_URL = "https://the-internet.herokuapp.com/login"


def test_login_valid(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.open(BASE_URL)
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert "Secure Area" in home_page.get_header_text()


def test_login_invalid(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)
    login_page.login("wrong", "wrong")

    assert "Your username is invalid!" in login_page.get_message()


def test_home_title(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    assert "The Internet" in driver.title

def test_login_visual(driver):

    driver.get(BASE_URL)

    visual = VisualValidator(driver, test_name="Login Visual Test")
    visual.start()

    #driver.execute_script("document.body.style.backgroundColor = 'red'")

    # Before Login
    visual.check("Login Page")

    login_page = LoginPage(driver)
    login_page.login("testuser", "password")

    # After Login
    visual.check("Dashboard UI")

    result = visual.close()
    
    allure.attach(
        str(result),
        name="Visual Result",
        attachment_type=allure.attachment_type.TEXT
    )

    assert result is not None