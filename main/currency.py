import requests
from django.conf import settings


def get_currency():

    EXCHANGERATE_API_KEY = settings.EXCHANGERATE_API_KEY
    URL_USD = f'https://v6.exchangerate-api.com/v6/{EXCHANGERATE_API_KEY}/latest/USD'
    URL_EUR = f'https://v6.exchangerate-api.com/v6/{EXCHANGERATE_API_KEY}/latest/EUR'
    response_USD = requests.get(url=URL_USD)
    response_EUR = requests.get(url=URL_EUR)
    USD = response_USD.json()['conversion_rates']['RUB']
    EUR = response_EUR.json()['conversion_rates']['RUB']

    OILPRICE_API_KEY = settings.OILPRICE_API_KEY
    URL_OILPRICE = "https://api.oilpriceapi.com/v1/prices/latest"

    headers = {
        "Authorization": f"Token {OILPRICE_API_KEY}"
    }

    response_OIL = requests.get(URL_OILPRICE, headers=headers)
    OIL = response_OIL.json()

    response_GOLD_USD =  requests.get(URL_OILPRICE, headers=headers, params={"code": "GOLD_USD", "unit": "g"})
    GOLD_USD = response_GOLD_USD.json()
    GOLD = float(GOLD_USD['data']['price']) / 31.1035 * USD

    result = {'USD': USD, 'EUR': EUR, 'Brent': OIL['data']['price'], 'Gold': round(GOLD)}

    return result