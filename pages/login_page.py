from base.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    MESSAGE = (By.ID,"flash")

    def open(self,url):
        self.driver.get(url)

    def login(self,username,password):
        self.fill(self.USERNAME,username)
        self.fill(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def get_message(self):
        return self.find(self.MESSAGE).text
