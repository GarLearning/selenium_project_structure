import sys
sys.path.append("./")
from browser_manager import BrowserManager
from pages.pages import Page
from data.handling import data
from selenium.common.exceptions import TimeoutException
from pages.pages import Page_1
from config import Config

browser_manager = BrowserManager()
browser = browser_manager.driver

page_test = Page (browser)

page_test.open("")

# Make commands to automate/test some task
# - Input some data and URLs
# - Enter commands from correspondent Class in pages.pages
