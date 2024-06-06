from selenium import webdriver
from config import Config


class BrowserManager:
    """
    A manager class for handling browser instances using Selenium WebDriver.

    Attributes:
        browser_type (str): The type of browser to use ('chrome' or 'firefox').
        driver (webdriver): The WebDriver instance.
    """
    def __init__(self, browser_type="chrome"):
        if browser_type.lower() == "chrome":
            self.driver = self.setup_chrome()

    def _chrome_options(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = Config.chrome_path
        return chrome_options

    def setup_chrome(self):
        driver = webdriver.Chrome(options=self._chrome_options())
        return driver

    def teardown(self):
        self.driver.quit()
