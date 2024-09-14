import requests
import json

from Secrets.secrets import TELEGRAM_TOKEN

URL = 'https://api.telegram.org/bot'

# https://telegram-bot-sdk.readme.io/reference/getme
result = json.dumps(requests.get(f'{URL}{TELEGRAM_TOKEN}/getMe').json(), indent=4)
print(result)