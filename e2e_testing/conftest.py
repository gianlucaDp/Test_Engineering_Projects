import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chrome_service

from e2e_testing.view.MainPage import MainPage


@pytest.fixture(scope="session", autouse=True)
def driver():
    driver = webdriver.Chrome(service=chrome_service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)
