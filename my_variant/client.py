from socket import socket, AF_INET, SOCK_STREAM
from common.config import *
from common.utils import *
import json

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

client_name = 'client'

s.send(send_message('client.json', 'presence').encode('utf-8')) # отсылаем на сервер

data = s.recv(4096) # получаем ответ от сервера, пишем его в переменную data
# print(data.decode('utf-8'))  # декодируем ответ и печатаем его

print(get_data_from_message(data)) # обрабатываем сообщение функцией(декодируем, переводим в словарь), получаем доступ к значениям
s.close()  # закрываем соединение