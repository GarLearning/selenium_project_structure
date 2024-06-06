from selenium.webdriver.common.by import By

class TagsLocator:
    """
    A utility class for locating various HTML tags on a webpage based in tag name.
    """
    a_tag = (By.TAG_NAME, "a")
    li_tag = (By.TAG_NAME, "li")
    span_tag = (By.TAG_NAME, "span")
    tr_tag = (By.TAG_NAME, "tr")
    td_tag = (By.TAG_NAME, "td")

class TypeLocators:
    """
    A class to abstract `By.CLASS_NAME` for use in Selenium actions.
    """
    class_name = (By.CLASS_NAME)
