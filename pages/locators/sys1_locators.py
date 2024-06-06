from selenium.webdriver.common.by import By

class FirstLocator:
    """
    Locators with belongs to First element component in sys1.
    """
    first = (By.CSS_SELECTOR, "[id='first']")

class SecondLocator:
    """
    Locators with belongs to Second element component in sys1.
    """
    second = (By.CSS_SELECTOR, "[id='second]'")
