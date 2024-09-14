import requests
import time

from Secrets.secrets import TELEGRAM_TOKEN

URL = 'https://api.telegram.org/bot'
SLEEP_TIME = 2

def get_updates(offset: int = 0):
    result = requests.get(f'{URL}{TELEGRAM_TOKEN}/getUpdates?offset={offset}').json()
    return result['result']

def send_message(chat_id: int, text: str):
    # https://telegram-bot-sdk.readme.io/reference/sendmessage
    requests.post(f'{URL}{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={text}')

def act_on_message(message: dict):
    print(f"ID пользователя: {message['message']['chat']['id']}, Сообщение: {message['message']['text']}")
    send_message(message['message']['chat']['id'], message['message']['text'])

def run():
    update_id = 0
    updates = get_updates()
    if updates:
        update_id = get_updates()[-1]['update_id']

    while True:
        time.sleep(SLEEP_TIME)
        messages = get_updates(update_id)

        for message in messages:
            if update_id <= message['update_id']:
                update_id = message['update_id'] + 1
                act_on_message(message)


if __name__ == '__main__':
    run()