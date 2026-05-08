from django.shortcuts import render
from config.settings import BASE_DIR
from main.currency import get_currency
from main.weather import get_weather
from django.utils import timezone


def get_greeting():
    hour = timezone.localtime().hour

    if 5 <= hour < 12:
        return "Доброе утро 🌄"
    elif 12 <= hour < 17:
        return "Добрый день ☀️"
    elif 17 <= hour < 23:
        return "Добрый вечер 🌄"
    else:
        return "Доброй ночи 🌚"

def main(request):
    weather = get_weather()
    greeting = get_greeting()
    currency = get_currency()

    return render(request, f"{BASE_DIR}/main/templates/main.html", {"weather": weather, 'greeting': greeting, 'currency': currency})