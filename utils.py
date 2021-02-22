import json
import sys
import os

def load_configs(is_server=True):
    config_keys = [
        'DEFAULT_PORT',
        'MAX_CONNECTIONS',
        'MAX_PACKAGE_LENGTH',
        'ENCODING',
        'ACTION',
        'TIME',
        'USER',
        'ACCOUNT_NAME',
        'PRESENCE',
        'RESPONSE',
        'ERROR',
        'SETTIMEOUT'
    ]
    if not is_server:
        config_keys.append('DEFAULT_IP_ADDRESS')
    if not os.path.exists('config.json'):
        print('Файл конфигурации не найден')
        sys.exit(1)
    with open('config.json') as config_file:
        CONFIGS = json.load(config_file)
    loaded_config_keys = list(CONFIGS.keys())
    for key in config_keys:
        if key not in loaded_config_keys:
            print(f'В файле конфигурации не хватает ключа: {key}')
            sys.exit(1)
    return CONFIGS


def send_message(opened_socket, message, CONFIGS):
    json_message = json.dumps(message)
    response = json_message.encode(CONFIGS.get('ENCODING'))
    opened_socket.send(response)

def get_message(opened_socket, CONFIGS):
    response = opened_socket.recv(int(CONFIGS.get('MAX_PACKAGE_LENGTH')))
    if isinstance(response, bytes):
        json_response = response.decode(CONFIGS.get('ENCODING'))
        response_dict = json.loads(json_response)
        if isinstance(response_dict, dict):
            return response_dict
        raise ValueError
    raise ValueError