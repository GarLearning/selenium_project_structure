from abc import ABC
from selenium.webdriver.support.ui import WebDriverWait
from pages_objects.custom_waits import  (
        amount_elements
    )
from selenium.webdriver.support.expected_conditions import (
        presence_of_all_elements_located,
        visibility_of_element_located,
        invisibility_of_element_located,
        element_to_be_clickable
    )

class SeleniumWaits:
    """
    Provide different waiting types, based in expected_conditions and custom wait.
    """
    def wait_elements(self, locator, wait_time, elements, attempts_interval):
        wait = WebDriverWait(self.webdriver, wait_time, poll_frequency=attempts_interval)
        wait.until(
            amount_elements(locator, elements),
            f"Not found the {elements} elements"
        )

    def presence_of_element(self, locator, wait_time, attempts_interval):
        wait = WebDriverWait(self.webdriver, wait_time, poll_frequency=attempts_interval)
        wait.until(
            presence_of_all_elements_located(locator),
            "Element not located"
        )
    
    def visibility_of_element(self, locator, wait_time, attempts_interval):
        wait = WebDriverWait(self.webdriver, wait_time, poll_frequency=attempts_interval)
        wait.until(
            visibility_of_element_located(locator),
            "Element not visible"
        )

    def invisibility_of_element_located(self, locator, wait_time, attempts_interval):
        wait = WebDriverWait(self.webdriver, wait_time, poll_frequency=attempts_interval)
        wait.until(
            invisibility_of_element_located(locator),
            "Element not visible"
        )
    
    def element_to_be_clickable(self, locator, wait_time, attempts_interval):
        wait = WebDriverWait(self.webdriver, wait_time, poll_frequency=attempts_interval)
        wait.until(
            element_to_be_clickable(locator),
            "Element not visible"
        )
    

class SeleniumObject(SeleniumWaits):
    """
    Provides methods to interact with web elements using Selenium WebDriver and custom wait conditions.
    """
    def find_element(self, locator, wait_time=20, wait_func= 'presence_of_element', attempts_interval=0.5):
        parameters = (locator, wait_time, attempts_interval)
        obj = getattr(self, wait_func)
        obj(*parameters)
        
        return self.webdriver.find_element(*locator)
    
    def find_elements(self, locator, wait_time=20, elements=1, wait_func= 'wait_elements', attempts_interval=0.5):
        parameters = (locator, wait_time, elements, attempts_interval)
        obj = getattr(self, wait_func)
        obj(*parameters)
        # self.wait_elements(locator, wait_time, elements)
        return self.webdriver.find_elements(*locator)
    
    def find_child_element(self, locator, parent):
        return parent.find_element(*locator)
    
    def find_child_elements(self, locator, parent):
        return parent.find_elements(*locator)
    
    def not_find_element(self, locator, wait_time=20, wait_func= 'invisibility_of_element_located', attempts_interval=0.5):
        parameters = (locator, wait_time, attempts_interval)
        obj = getattr(self, wait_func)
        obj(*parameters)

class Page(ABC, SeleniumObject):
    """
    Represents a web page in the Selenium framework.

    Initializes the Page object with the provided WebDriver.
    Opens the specified URL using the WebDriver.
    Reflects the PageElement attributes and assigns the WebDriver to them.

    """
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self._reflection()

    def open(self, url=''):
        self.webdriver.get(url)

    def _reflection(self):
        for attribute in dir(self):
            real_attribute = getattr(self, attribute)
            if isinstance(real_attribute,PageElement):
                real_attribute.webdriver = self.webdriver


class PageElement(ABC, SeleniumObject):
    """
    Represents an element on a web page in the Selenium framework.

    This class provides methods to interact with the web element.
    """
    def __init__(self, webdriver=None):
        self.webdriver = webdriver
