from django.core.cache import cache
from redis.exceptions import RedisError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.currency import get_currency
from main.news import get_news
from main.weather import get_weather


WEATHER_CACHE_KEY = 'main:weather:kochenyovo'
MARKETS_CACHE_KEY = 'main:markets'
NEWS_CACHE_KEY = 'main:news'
WEATHER_CACHE_TTL = 60 * 60 * 2
MARKETS_CACHE_TTL = 60 * 60 * 6
NEWS_CACHE_TTL = 60 * 60 * 2


class WeatherAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = get_cached_value(WEATHER_CACHE_KEY)

        if data is None:
            data = get_weather()
            set_cached_value(WEATHER_CACHE_KEY, data, WEATHER_CACHE_TTL)

        return Response(data)


class MarketsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = get_cached_value(MARKETS_CACHE_KEY)

        if data is None:
            data = get_currency()
            set_cached_value(MARKETS_CACHE_KEY, data, MARKETS_CACHE_TTL)

        return Response(data)


class NewsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = get_cached_value(NEWS_CACHE_KEY)

        if data is None:
            data = get_news(limit=3)
            set_cached_value(NEWS_CACHE_KEY, data, NEWS_CACHE_TTL)

        return Response(data)


def get_cached_value(key):
    try:
        return cache.get(key)
    except RedisError:
        return None


def set_cached_value(key, value, timeout):
    try:
        cache.set(key, value, timeout)
    except RedisError:
        pass
