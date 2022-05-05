import requests

from api_testing.requests.BaseRequests import BASE_URL, handle_response


@handle_response
def create_deck():
    return requests.get(f"{BASE_URL}/deck/new/")


@handle_response
def shuffle_deck(deck_id: str):
    return requests.get(f"{BASE_URL}/deck/{deck_id}/shuffle/")


@handle_response
def draw_cards(deck_id: str, num_cards: int):
    params = {"count": num_cards}
    return requests.get(f"{BASE_URL}/deck/{deck_id}/draw/", params=params)


@handle_response
def add_to_pile(deck_id: str, pile_name: str, cards: str):
    params = {"cards": cards}
    return requests.get(f"{BASE_URL}/deck/{deck_id}/pile/{pile_name}/add/", params=params)
