import json

BASE_URL = "http://deckofcardsapi.com/api/"


def handle_response(function):
    """
    Decorator to convert the response into a JSON object. It raises an error if the request is not successful
    """

    def inner(*args, **kwargs):
        response = function(*args, **kwargs)
        response.raise_for_status()
        json_response = json.loads(response.text)
        if not json_response["success"]:
            raise Exception("Request failed")
        return json_response
    return inner
