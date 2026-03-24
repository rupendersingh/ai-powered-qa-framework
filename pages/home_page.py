from selenium.webdriver.common.by import By
from base.base_page import BasePage

class HomePage(BasePage):
    HEADER = (By.TAG_NAME,"h2")
    
    def get_header_text(self):
        return self.find(self.HEADER).text