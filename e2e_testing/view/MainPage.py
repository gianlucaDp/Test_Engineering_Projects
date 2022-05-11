import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from e2e_testing.objects.Locator import Locator
from e2e_testing.objects.Tile import Tile
from e2e_testing.view.BaseView import BaseView

MOVE_WAIT_TIME = 0.5


class MainPage(BaseView):
    """
    Class with the actions that need to be done into the main page
    """

    RESTART_ITEM = Locator(By.XPATH, r"//a[@href='./']")
    BOARD_ITEM = Locator(By.XPATH, r"//div[@id='board']")
    TILE_ITEM = Locator(By.XPATH, BOARD_ITEM.locator + r"//img[@name='space{position}']")
    MESSAGE_ITEM = Locator(By.ID, "message")
    MOVING_PLAYER_ITEM = Locator(By.XPATH, BOARD_ITEM.locator + r"//img[contains(@src,'you2')]")
    MOVING_OPPONENT_ITEM = Locator(By.XPATH, BOARD_ITEM.locator + r"//img[contains(@src,'me2')]")

    def __init__(self, driver: WebDriver):
        """
        Constructor of the page, it load the page and waits that the main elements are loaded
        :param driver: Selenium Chrome WebDriver
        """
        super().__init__(driver)
        driver.get("https://www.gamesforthebrain.com/game/checkers/")
        self.wait_for(self.BOARD_ITEM())
        self.wait_for(self.RESTART_ITEM())

    def get_tile(self, position: str) -> Tile:
        """
        Get the tile at a given position
        NOTE: The position can be found in attribute name of any tile, right after the word "space"
        :param position: tile position
        :return: WebElement of the tile
        """
        return Tile(self.find(self.TILE_ITEM(position=position)))

    def player_can_move(self) -> bool:
        """
         Check if it's player turn to move
         :return: True if it is player turn False otherwise
         """
        msg1 = "Select an orange piece to move."
        msg2 = "Make a move."
        element = self.find(self.MESSAGE_ITEM())
        return element.text in (msg2, msg1) and not self.opponent_moving()

    def move_player_piece(self, start: str, destination: str) -> bool:
        """
        Move a player from a tile to another.
        Function raises exception if invalid start or destination points are selected
        NOTE: The positions can be found in attribute name of any tile, right after the word "space"
        :param start: The position of the piece to move (must be a player controlled tile)
        :param destination: The position to reach (must be an empty tile)
        :return: True if the movement was successful False otherwise
        """
        tile = self.get_tile(start)
        if not tile.is_player():
            raise ValueError("Cannot move other than player pieces")
        tile.element.click()
        tile = self.get_tile(destination)
        tile.element.click()
        self.wait_for_player()
        # The movement can be considered successful if the starting position is empty or with an opponent piece
        tile = self.get_tile(start)
        return not tile.is_player()

    def wait_for_opponent(self, tries=3):
        """
        Wait for opponent to complete his turn
        :param tries: How many time it should try to wait before returning
        """
        if tries <= 0:
            return
        else:
            time.sleep(MOVE_WAIT_TIME)
            tries -= 1
            if not self.player_can_move():
                self.wait_for_opponent(tries)

    def wait_for_player(self, tries=3):
        """
        Wait for player to complete his action
        :param tries: How many time it should try to wait before returning
        """
        if tries <= 0:
            return
        else:
            time.sleep(MOVE_WAIT_TIME)
            tries -= 1
            if self.player_moving():
                self.wait_for_player(tries)

    def player_moving(self) -> bool:
        """
        Check if player's piece movement is in progress
        :return: True if player's piece is still highlighted, False otherwise
        """
        return bool(self.find_multiple(self.MOVING_PLAYER_ITEM()))

    def opponent_moving(self) -> bool:
        """
        Check if opponent's piece movement is in progress
        :return: True if opponent's piece is still highlighted, False otherwise
        """
        return bool(self.find_multiple(self.MOVING_OPPONENT_ITEM()))

    def restart_game(self):
        """
        Move the piece on the board at the default initial configuration
        """
        self.find(self.RESTART_ITEM()).click()
