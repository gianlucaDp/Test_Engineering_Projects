from selenium.webdriver.common.by import By

from e2e_testing.objects.Locator import Locator
from e2e_testing.view.BaseView import BaseView


class MainPage(BaseView):
    RESTART_ITEM = Locator(By.XPATH, r"//a[@href='./']")
    BOARD_ITEM = Locator(By.XPATH, r"//div[@id='board']")
    ROW_ITEM = Locator(By.XPATH, BOARD_ITEM.locator + r"/div[@class='line'][{line}]")
    IMG_ITEM = Locator(By.XPATH, BOARD_ITEM.locator + r"/img[@name='space{column}{row}'")

    def __init__(self, driver):
        super().__init__(driver)
        driver.get("https://www.gamesforthebrain.com/game/checkers/")

