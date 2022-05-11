from selenium.webdriver.remote.webelement import WebElement


class Tile:
    """
    Class with the checks that can be done on a tile.
    ...
    Attributes
    ----------
    element : WebElement
        WebElement of the tile
    """

    def __init__(self, element: WebElement):
        self.element = element

    def is_player(self) -> bool:
        """
        Check if the tile is a player piece
        :return: True if the tile contains is a player piece False otherwise
        """
        src = self.element.get_attribute("src")
        return src.endswith("you1.gif") or src.endswith("you2.gif")

    def is_opponent(self) -> bool:
        """
         Check if the tile is an opponent piece
         :return: True if the tile contains an opponent piece False otherwise
         """
        src = self.element.get_attribute("src")
        return src.endswith("me1.gif") or src.endswith("me2.gif")

    def is_free(self) -> bool:
        """
         Check if the tile does not contain any piece
         :return: True if it is empty False otherwise
         """
        return not (self.is_player() or self.is_opponent())
