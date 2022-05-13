import requests

from rest_testing.requests.BaseRequests import BASE_URL, handle_response


@handle_response
def list_cards(deck_id: str, pile_name: str):
    return requests.get(f"{BASE_URL}/deck/{deck_id}/pile/{pile_name}/list/")


@handle_response
def shuffle(deck_id: str, pile_name: str):
    return requests.get(f"{BASE_URL}/deck/{deck_id}/pile/{pile_name}/shuffle/")


@handle_response
def draw_cards(deck_id: str, pile_name: str, num_cards: int):
    params = {"count": num_cards}
    return requests.get(f"{BASE_URL}/deck/{deck_id}/pile/{pile_name}/draw/", params=params)
