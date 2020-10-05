import requests
from .models import Quote

url = "https://vector-restful-api.herokuapp.com/vector/api/v1.0/quotes/1"

def get_quote():
    """
    Function to consume http request and return a Quote class instance
    """
    response = requests.get(url).json()

    random_quote = Quote(response.get("author"), response.get("description"))
    return random_quote