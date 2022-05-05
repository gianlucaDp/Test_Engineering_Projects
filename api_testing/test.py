from api_testing.objects.Deck import Deck


def test_draw_divide_shuffle():
    """
    Test the website main API endpoints
    """

    deck = Deck()
    assert deck.remaining_cards == 52

    deck.shuffle()
    assert deck.shuffled is True

    deck.draw_cards(3)
    assert deck.remaining_cards == 49
    print("\n\n")

    cards_1 = deck.draw_cards(5)
    pile1 = deck.add_to_pile("pile1", cards_1)
    pile1_cards = pile1.cards
    print("PILE 1: ", pile1_cards)
    assert len(pile1_cards) == 5

    cards_2 = deck.draw_cards(5)
    pile2 = deck.add_to_pile("pile2", cards_2)
    pile2_cards = pile2.cards
    print("PILE 2: ", pile2.cards)
    assert len(pile2_cards) == 5

    pile1.shuffle()
    assert pile1_cards != pile1.cards

    pile1.draw_cards(2)
    assert len(pile1.cards) == 3

    pile2.draw_cards(3)
    assert len(pile2.cards) == 2
