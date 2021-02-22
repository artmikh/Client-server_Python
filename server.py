import json
from os import truncate
import sys
from socket import socket, AF_INET, SOCK_STREAM
# import log.server_log_config
# import logging
from utils import load_configs, send_message, get_message
# from decorators import Logg
import select

CONFIGS = dict()

# logger = logging.getLogger('app_server')
# logger.setLevel(logging.DEBUG)
# Logg = decorators.Logg

def read_requests(r_list, clients):
    responses = {}

    for sock in r_list:
        try:
            data = get_message(sock, CONFIGS)
            responses[sock] = data
        except:
            clients.remove(sock)
    
    return responses

def write_responses(requests, w_list, clients):
    for sock in w_list:
        if sock in requests:
            try:
                send_message(sock, requests[sock], CONFIGS) 
            except:
                sock.close()
                clients.remove(sock)




# @Logg()
# def handle_message(message):
#     if CONFIGS.get('ACTION') in message and message[CONFIGS.get('ACTION')] == CONFIGS.get('PRESENCE') and CONFIGS.get('TIME') in message and CONFIGS.get('USER') in message and message[CONFIGS.get('USER')][CONFIGS.get('ACCOUNT_NAME')] == 'Guest':
#         return {CONFIGS.get('RESPONSE'): 200}
#     return {
#         CONFIGS.get('RESPONSE'): 400,
#         CONFIGS.get('ERROR'): 'Bad Request'
#     }

def main():
    global CONFIGS
    CONFIGS = load_configs()
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = CONFIGS.get('DEFAULT_PORT')
        if not 65535 >= listen_port >= 1024:
            raise ValueError
    except IndexError:
        # logger.critical('После -\'p\' необходимо указать порт')
        print('После -\'p\' необходимо указать порт')
        sys.exit(1)
    except ValueError:
        # logger.critical('Порт должен быть указан в пределах от 1024 до 65535')
        print('Порт должен быть указан в пределах от 1024 до 65535')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''

    except IndexError:
        # logger.critical('После -\'a\' необходимо указать адрес для ')
        print('После -\'a\' необходимо указать адрес для ')
        sys.exit(1)

    transport = socket(AF_INET, SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    transport.listen(CONFIGS.get('MAX_CONNECTIONS'))
    # transport.settimeout(CONFIGS.get('SETTIMEOUT'))
    transport.settimeout(1)

    clients = []

    while True:
        try: 
            client, client_address = transport.accept()
        except OSError:
            pass
        else:
            clients.append(client)
        finally:
            r_list = []
            w_list = []

            try:
                r_list, w_list, e_list = select.select(clients, clients, [], 1)
            except:
                pass

            requests = read_requests(r_list, clients)
            if requests:
                write_responses(requests, w_list, clients)


        # try:
        #     message = get_message(client, CONFIGS)
        #     response = handle_message(message)
        #     logger.info(f'Ответ клиента: ({response})')
        #     send_message(client, response, CONFIGS)
        #     client.close()
        # except (ValueError, json.JSONDecodeError):
        #     logger.error('Принято некорректное сообщение от клиента')
        #     # print('Принято некорректное сообщение от клиента')
        #     client.close()

print('server start')
if __name__ == '__main__':
    main()