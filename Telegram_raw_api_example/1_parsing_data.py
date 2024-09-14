import requests
import json

from Secrets.secrets import TELEGRAM_TOKEN

URL = 'https://api.telegram.org/bot'

def get_messages():
    # https://telegram-bot-sdk.readme.io/reference/getupdates
    result = requests.get(f'{URL}{TELEGRAM_TOKEN}/getUpdates').json()

    print(f'Получен объект: {result}')
    return result['result']

messages = get_messages()
for message in messages:
    print("================")
    print(json.dumps(message, indent=4))
