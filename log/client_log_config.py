import logging
from logging import handlers

logger = logging.getLogger('app_client')

formatter = logging.Formatter('%(asctime)s %(levelname)-10s %(module)s %(message)s')

file_handler = logging.FileHandler('log/client_logging/client.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# log.addHandler(handlers.TimedRotatingFileHandler('client.log', when='', delay=''))


# def logg(func):
#     def wrapper(*args, **kwargs):
#         print('console log')
#         logger.info(f'Функция {func.__name__} вызвана из функции main')
#         r = func(*args, **kwargs)
#         return r
#     return wrapper

