import inspect
import logging
import sys
import traceback

if sys.argv[0].find('client') == -1:
    logger = logging.getLogger('app_server')
else:
    logger = logging.getLogger('app_client')

print('decorator')

class Logg(): 
    def __call__(self, func):
        def decorator(*args, **kwargs):
            print(logger)
            r = func(*args, **kwargs)
            logger.debug(f'Функция: {func.__name__}. '
                         f'Параметры: {args}, {kwargs}. '
                         f'Модуль: {func.__module__}'
                         f'Вызов из функции {traceback.format_stack()[0].strip().split()[-1]}. '
                         f'Вызов из функции {inspect.stack()[1][3]}')
            return r
        return decorator