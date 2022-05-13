class Card:
    """
    A container class for cards
    ...
    Attributes
    ----------
    code : str
        ID to identify the card
    value : str
        value of the card
    suit : str
        suit of the card
    """

    def __init__(self, code: str, value: str, suit: str):
        self.code = code
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"<{self.code}> {self.value} - {self.suit}"

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.code == other.code
