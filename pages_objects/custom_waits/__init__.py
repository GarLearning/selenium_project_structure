class amount_elements:
  """
    Waits until a specific amount of elements are present.

    This custom wait method uses Selenium WebDriver to wait until the specified number of elements
    identified by the given locator are present on the webpage.

    Args:
        locator (tuple): A tuple representing the locator strategy and locator value (e.g., (By.CLASS_NAME, 'example')).
        elements (int): The expected number of elements to wait for.
        
    Returns:
        list[WebElement]: A list of WebElements found that match the locator and meet the specified amount.
    """
  def __init__(self, locator, elements):
    self.locator = locator
    self.elements = elements

  def __call__(self, driver):
    element = driver.find_elements(*self.locator)
    if len(driver.find_elements(*self.locator)) >= self.elements:
        return element
    return False