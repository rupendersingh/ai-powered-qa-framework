import os
from applitools.selenium import Eyes

class VisualValidator:
    def __init__(self,driver, test_name = "Visual Test"):
        self.driver = driver
        self.eyes = Eyes()
        self.eyes.api_key = os.getenv('APPLITOOLS_API_KEY')
        self.test_name = test_name

    def start(self, app_name = "AI QA Framework"):
        self.eyes.open(self.driver, app_name, self.test_name)

    def check(self, name="Checkpoint"):
        self.eyes.check_window(name)

    def close(self):
        try:
            result = self.eyes.close()
            return result
        finally:
            self.eyes.abort_if_not_closed()