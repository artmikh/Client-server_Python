import logging
from logging import handlers

logger = logging.getLogger('app_server')

formatter = logging.Formatter('%(asctime)s %(levelname)-10s %(module)s %(message)s')

file_handler = handlers.TimedRotatingFileHandler('log/server_logging/server.log', when='D', interval=1, encoding='utf-8', )
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)


class Logg():
    
    def __init__(self, levelname='INFO'):
        self.levelname = levelname
        # pass
    
    def __call__(self, func):
        def decorator(*args, **kwargs):
            # logger.setLevel(logging.(self.levelname))
            print(f' server {self.levelname}')
            logger.info(f'Функция {func.__name__} вызвана из функции main')
            r = func(*args, **kwargs)
            return r
        return decorator
