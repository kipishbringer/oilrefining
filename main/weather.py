# import requests
# from django.conf import settings


def get_weather():
    # url = "https://api.openweathermap.org/data/2.5/weather"
    #
    # params = {
    #     "q": city,
    #     "appid": settings.OPENWEATHER_API_KEY,
    #     "units": "metric",
    #     "lang": "ru"
    # }
    #
    # response = requests.get(url, params=params)
    # return response.json()
    weather = {'coord': {'lon': 82.237, 'lat': 55.0083},
               'weather': [{'id': 802, 'main': 'Clouds', 'description': 'переменная облачность', 'icon': '03d'}],
               'base': 'stations',
               'main': {'temp': 20.61, 'feels_like': 19.72, 'temp_min': 20.61, 'temp_max': 20.61, 'pressure': 1014, 'humidity': 38, 'sea_level': 1014, 'grnd_level': 995},
               'visibility': 10000,
               'wind': {'speed': 4.36, 'deg': 263, 'gust': 5.59},
               'clouds': {'all': 33},
               'dt': 1778156356,
               'sys': {'type': 1, 'id': 8958, 'country': 'RU', 'sunrise': 1778107148, 'sunset': 1778163365},
               'timezone': 25200, 'id': 1503082, 'name': 'Коченёво', 'cod': 200}

    return weather