from django.shortcuts import render
from config.settings import BASE_DIR


def main(request):
    return render(request, f"{BASE_DIR}/main/templates/main.html")