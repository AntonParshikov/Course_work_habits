import requests

from config.settings import TELEGRAM_TOKEN


def get_updates():
    response = requests.get(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates')
    return response.json()
