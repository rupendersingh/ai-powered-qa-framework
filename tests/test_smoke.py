from base.base_test import BaseTest

class TestSmoke(BaseTest):
    def test_open_google(self):
        self.driver.get("https://www.google.com")
        assert "Google" in self.driver.title