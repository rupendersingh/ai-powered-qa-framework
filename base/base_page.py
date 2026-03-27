import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.smart_locator import try_locators

class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    @allure.step("Find element : {locator}")
    def find(self, locator):

        # If list → healing
        if isinstance(locator, list):
            return try_locators(self.driver, locator)

        # If tuple → normal
        if isinstance(locator, tuple):
            return self.wait.until(EC.presence_of_element_located(locator))

        raise Exception(f"Invalid locator format: {locator}")
    
    @allure.step("Click element : {locator}")
    def click(self,locator):
        self.find(locator).click()

    @allure.step("Fill element: {locator} with value: {text}")
    def fill(self,locator,text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)