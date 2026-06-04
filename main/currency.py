from django.conf import settings
import requests


def get_currency():
    exchangerate_api_key = settings.EXCHANGERATE_API_KEY
    oilprice_api_key = settings.OILPRICE_API_KEY
    url_usd = f'https://v6.exchangerate-api.com/v6/{exchangerate_api_key}/latest/USD'
    url_eur = f'https://v6.exchangerate-api.com/v6/{exchangerate_api_key}/latest/EUR'
    response_usd = requests.get(url=url_usd, timeout=10)
    response_eur = requests.get(url=url_eur, timeout=10)
    response_usd.raise_for_status()
    response_eur.raise_for_status()

    usd = response_usd.json()['conversion_rates']['RUB']
    eur = response_eur.json()['conversion_rates']['RUB']

    headers = {
        "Authorization": f"Token {oilprice_api_key}"
    }

    oilprice_url = "https://api.oilpriceapi.com/v1/prices/latest"
    response_oil = requests.get(oilprice_url, headers=headers, timeout=10)
    response_gold_usd = requests.get(oilprice_url, headers=headers, params={"code": "GOLD_USD", "unit": "g"}, timeout=10)
    response_oil.raise_for_status()
    response_gold_usd.raise_for_status()

    oil = response_oil.json()
    gold_usd = response_gold_usd.json()
    gold = float(gold_usd['data']['price']) * usd

    return {'USD': usd, 'EUR': eur, 'Brent': oil['data']['price'], 'Gold': round(gold)}
