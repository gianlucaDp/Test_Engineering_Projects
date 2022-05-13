from typing import List

import rest_testing.requests.DeckRequests as Dr
from rest_testing.objects.Card import Card
from rest_testing.objects.Pile import Pile


class Deck:
    """
    A class used to test Deck API
    ...
    Attributes
    ----------
    deck_id : str
        ID to identify the deck
    remaining_cards : int
        Number of remaining cards in the deck
    shuffled : bool
        True if the deck has been shuffled
    """

    def __init__(self, deck_id: str = ""):
        """
        Constructor of the class, if no ID is supplied it creates a new deck with the API
        """
        if deck_id:
            self.deck_id = deck_id
            self.remaining_cards = None
        else:
            json_response = Dr.create_deck()
            self.deck_id = json_response["deck_id"]
            self.remaining_cards = json_response["remaining"]
        self.shuffled = False

    def shuffle(self):
        """
        Calls the API to shuffle the deck
        """
        json_response = Dr.shuffle_deck(self.deck_id)
        self.shuffled = json_response["shuffled"]

    def draw_cards(self, num_cards: int = 1) -> List[Card]:
        """
        Calls the API to draw a number of cards from the deck
        :param num_cards: Number of cards to draw
        :return: Picked cards
        """
        json_response = Dr.draw_cards(self.deck_id, num_cards)
        self.remaining_cards = json_response["remaining"]
        return [Card(c["code"], c["value"], c["suit"]) for c in json_response["cards"]]

    def add_to_pile(self, pile_name: str, cards: List[Card]) -> Pile:
        """
        Calls the API to add a list of cards to a pile. If the pile does not exist it will be created
        :param pile_name: Name of the pile to create
        :param cards: Cards to be added to the pile
        :return: Pile object
        """
        cards_code = ",".join(card.code for card in cards)
        json_response = Dr.add_to_pile(self.deck_id, pile_name, cards_code)
        pile = Pile(self.deck_id, pile_name)
        pile.remaining_cards = json_response["piles"][pile_name]["remaining"]
        return pile
