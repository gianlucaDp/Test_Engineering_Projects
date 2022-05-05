from typing import List

from api_testing.objects.Card import Card
import api_testing.requests.PileRequests as Pr


class Pile:
    """
    A class used to test Pile API
    ...
    Attributes
    ----------
    deck_id : str
        ID to identify the deck
    name : str
        name of the pile
    remaining_cards : int
        Number of remaining cards in the pile
    """

    def __init__(self, deck_id: str, name: str):
        self.deck_id = deck_id
        self.name = name
        self.remaining_cards = 0

    @property
    def cards(self) -> List[Card]:
        """
        Calls the API to get the list of cards into the pile
        :return: Available cards in the pile
        """
        json_response = Pr.list_cards(self.deck_id, self.name)
        self.remaining_cards = json_response["piles"][self.name]["remaining"]
        return [Card(c["code"], c["value"], c["suit"]) for c in json_response["piles"][self.name]["cards"]]

    def shuffle(self):
        """
        Calls the API to shuffle the pile
        """
        Pr.shuffle(self.deck_id, self.name)

    def draw_cards(self, num_cards: int = 1) -> List[Card]:
        """
        Calls the API to draw a number of cards from the pile
        :param num_cards: Number of cards to draw
        :return: Picked cards
        """
        json_response = Pr.draw_cards(self.deck_id, self.name, num_cards)
        self.remaining_cards = json_response["piles"][self.name]["remaining"]
        return [Card(c["code"], c["value"], c["suit"]) for c in json_response["cards"]]
