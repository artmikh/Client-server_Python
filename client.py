import json
from json.decoder import JSONDecodeError
from server import handle_message
import sys
from socket import socket, AF_INET, SOCK_STREAM
import time

from utils import *

CONFIGS = dict()

def create_presence_message(account_name):
    message = {
        CONFIGS.get('ACTIONS'): CONFIGS.get('PRESENCE'),
        CONFIGS.get('TIME'): time.time(),
        CONFIGS.get('USER'): {
            CONFIGS.get('ACCOUNT_NAME'): account_name
        }
    }
    return message

def handle_response(message):
    if CONFIGS.get('RESPONSE') in message:
        if message[CONFIGS.get('RESPONSE')] ==200:
            return '200 : ok'
        return f'401({message[CONFIGS.get("RESPONSE")]}) : {message[CONFIGS.get("ERROR")]}'
    raise ValueError

def main():
    global CONFIGS
    CONFIGS = load_configs(is_server=False)
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if not 65535 >= server_port >= 1024:
            raise ValueError
    except IndexError:
        server_address = CONFIGS.get('DEFAULT_IP_ADDRESS')
        server_port = CONFIGS.get('DEFAULT_PORT')
    except ValueError:
        print('Порт должен быть в пределах от 1024 до 65535')
        sys.exit(1)

    transport = socket(AF_INET, SOCK_STREAM)
    transport.connect((server_address, server_port))
    presence_message = create_presence_message('Guest')
    send_message(transport, presence_message, CONFIGS)
    try:
        response = get_message(transport, CONFIGS)
        handled_response = handle_response(response)
        print(f'Ответ от сервера: {response}')
        print(handled_response)
    except (ValueError, JSONDecodeError):
        print('Ошибка декодирования сообщения')

if __name__ == '__main__':
    main()