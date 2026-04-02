from base.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        
    USERNAME = [
    (By.ID, "THIS_WILL_NEVER_EXIST_123"),
    (By.NAME, "username"),
    (By.XPATH, "//input[@type='text']")
]

    PASSWORD = [
        (By.CSS_SELECTOR, "#password"),
        (By.XPATH, "//input[@id='password']")
    ]

    SUBMIT = [
        (By.CSS_SELECTOR, "#submit"),
        (By.XPATH, "//button[@type='submit']")
    ]


    MESSAGE = (By.ID,"flash")

    def open(self,url):
        self.driver.get(url)

    def login(self,username,password):
        self.fill(self.USERNAME,username)
        self.fill(self.PASSWORD,password)
        self.click(self.SUBMIT)

    def get_message(self):
        return self.find(self.MESSAGE).text
