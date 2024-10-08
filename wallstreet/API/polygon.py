from dotenv import load_dotenv
import requests
import os


load_dotenv()


def stock_detailed(ticket):
    url = f'https://api.polygon.io/v3/reference/tickers/{ticket}?apiKey={os.getenv('API_key')}'
    response = requests.get(url)
    get_full_name = response.json()['results']['name']
    return get_full_name.upper()
