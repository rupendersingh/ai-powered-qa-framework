from base.base_test import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage

class TestLogin(BaseTest):
    BASE_URL = "https://the-internet.herokuapp.com/login"

    def test_login_valid(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)

        login_page.open(self.BASE_URL)
        login_page.login("tomsmith", "SuperSecretPassword!")

        assert "Secure Area" in home_page.get_header_text()

        def test_login_invalid(self):
            login_page = LoginPage(self.driver)
            login_page.open(self.BASE_URL)

            login_page.login("wrong","wrong")
            assert "Your username is invalid!" in login_page.get_message()

        def test_home_title(self):
            login_page = LoginPage(self.driver)
            login_page.open(self.BASE_URL)

            assert "Login Page" in self.driver.title
