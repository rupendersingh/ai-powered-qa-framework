from pages.home_page import HomePage
from pages.login_page import LoginPage

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

    assert "Login Page" in driver.title