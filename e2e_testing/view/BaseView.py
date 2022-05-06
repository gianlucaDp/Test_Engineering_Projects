from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseView:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_multiple(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
