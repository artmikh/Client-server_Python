import logging
from logging import handlers

logger = logging.getLogger('app_server')

formatter = logging.Formatter('%(asctime)s %(levelname)-10s %(module)s %(message)s')

file_handler = handlers.TimedRotatingFileHandler('log/server_logging/server.log', when='D', interval=1, encoding='utf-8', )
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)
