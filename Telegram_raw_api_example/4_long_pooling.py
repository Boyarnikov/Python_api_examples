import requests
import time

from Secrets.secrets import TELEGRAM_TOKEN

URL = 'https://api.telegram.org/bot'
POOL_TIME = 10

def get_updates(offset: int = 0, timeout = POOL_TIME):
    print("send request")
    result = requests.get(f'{URL}{TELEGRAM_TOKEN}/getUpdates?offset={offset}&timeout={timeout}').json()
    return result['result']

def send_message(chat_id: int, text: str):
    requests.post(f'{URL}{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={text}')

def act_on_message(message: dict):
    print(f"ID пользователя: {message['message']['chat']['id']}, Сообщение: {message['message']['text']}")
    send_message(message['message']['chat']['id'], message['message']['text'])

def run():
    update_id = 0

    while True:
        messages = get_updates(offset = update_id)
        print(f"got updates with update_id={update_id}: {len(messages)}")

        for message in messages:
            if update_id <= message['update_id']:
                update_id = message['update_id'] + 1
                act_on_message(message)


if __name__ == '__main__':
    run()