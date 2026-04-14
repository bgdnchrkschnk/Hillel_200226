import logging

# # Налаштування конфігурації логування
# logging.basicConfig(filename="example.log", level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s %(filename)s:%(lineno)d')
#
# Логування подій різного рівня (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logging.debug('Це повідомлення рівня DEBUG') # 5 DEBUG LOG
logging.info('Це повідомлення рівня INFO') # 4 INFO LOG
logging.warning('Це повідомлення рівня WARNING') # 3 WARNING LOG
logging.error('Це повідомлення рівня ERROR') # 2 ERROR LOG
logging.critical('Це повідомлення рівня CRITICAL') # 1 CRITICAL LOG


import logging

# Створення конфігурації
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.StreamHandler(),  # Виведення в консоль
                        logging.FileHandler('example.log')  # Запис у файл
                    ])

# Використання логера
logger = logging.getLogger(__name__)

logger.debug('Це повідомлення рівня DEBUG')
logger.info('Це повідомлення рівня INFO')