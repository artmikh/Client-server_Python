from socket import socket, AF_INET, SOCK_STREAM
from my_variant.common.config import PORT
from my_variant.common.utils import *

def main(port=PORT):
    print('run')
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', port))
    s.listen(4)

    while True:
        client, addr = s.accept()
        print(str(addr))

        data = client.recv(4096) # получаем сообщение от клиента
        print(get_data_from_message(data)['action']) # обрабатываем сообщение функцией(декодируем, переводим в словарь), получаем доступ к значениям
        

        client.send(send_message('server.json', '1**/2**').encode('utf-8')) # отправляем сообщение клиенту из файла ответов сервера
        client.close()


if __name__ == '__main__':
    main()