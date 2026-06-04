import requests
from django.conf import settings


def get_weather():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": 55.0083,
        "lon": 82.237,
        "appid": settings.OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "ru",
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()
