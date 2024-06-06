import sys
sys.path.append("./")
from pages_objects import Page
from .elements import (
    Option1,
    Option2,
    Option3,
    Option4,
)

class Page_1(Page):
    """
    class imports as variable to be used in actions.
    """
    option_1 = Option1()
    option_2 = Option2()

class Page_2(Page):
    """
    class imports as variable to be used in actions.
    """
    option_3 = Option3()
    option_4 = Option4()
