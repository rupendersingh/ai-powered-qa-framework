class BaseTest:

    def take_screenshot(self, driver, name="screenshot.png"):
        driver.save_screenshot(name)
        return name