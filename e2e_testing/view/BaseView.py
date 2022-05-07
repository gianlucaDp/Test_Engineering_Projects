from typing import Tuple, List

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseView:
    """
    Class with basic actions that apply to all pages
    ...
    Attributes
    ----------
    driver : WebDriver
         WebDriver that will be used to automate the test
    wait : WebDriverWait
        Default wait of the driver, can be used when waiting for elements
    """

    def __init__(self, driver: WebDriver, wait: int = 3):
        """
        Constructor of the base view
        :param driver: Selenium Chrome WebDriver
        :param wait: How long the driver should wait for an element to appear
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, wait)

    def find(self, locator: Tuple[str, str]) -> WebElement:
        """
        Find an element in the page
        :param locator: tuple containing the locator type and string
        :return: Element if found, otherwise a NoSuchElementException is raised
        """
        return self.driver.find_element(*locator)

    def find_multiple(self, locator: Tuple[str, str]) -> List[WebElement]:
        """
        Find multiple elements in the page
        :param locator: tuple containing the locator type and string
        :return: List of founds element, can be empty if no element found
        """
        return self.driver.find_elements(*locator)

    def wait_for(self, locator: Tuple[str, str]) -> WebElement:
        """
        Wait for an element in the page
        :param locator: tuple containing the locator type and string
        :return: Element if found before timeout, otherwise a TimeoutException is raised
        """
        return self.wait.until(EC.presence_of_element_located(locator))
