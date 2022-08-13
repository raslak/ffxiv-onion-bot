import requests
from bs4 import BeautifulSoup


def find_cheapest_onion() -> str:
    URL = 'https://universalis.app/market/8166'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    try:
        cheapest_div = soup.find('div', class_='cheapest_price')
        cheapest_price_info = cheapest_div.find('span', class_='cheapest_price_info').text
    except Exception as e:
        cheapest_price_info = 'Unable to find price'

    return cheapest_price_info
