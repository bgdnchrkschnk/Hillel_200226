import logging

# Створення логера
custom_logger_file = logging.getLogger("custom_logger_file")

# Налаштування рівня логування
custom_logger_file.setLevel(logging.DEBUG)
#
# Створення обробника для запису в файл
file_handler = logging.FileHandler("//../../custom_logger_file.log")

# Налаштування рівня логування для обробника
file_handler.setLevel(logging.INFO)

# Створення форматера для обробника
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s %(filename)s:%(lineno)d')

file_handler.setFormatter(formatter)

# Додавання обробника до логера
custom_logger_file.addHandler(file_handler)

# Логування подій
custom_logger_file.debug('Це повідомлення рівня DEBUG')
custom_logger_file.info('Це повідомлення рівня INFO')
custom_logger_file.warning('Це повідомлення рівня WARNING')
custom_logger_file.error('Це повідомлення рівня ERROR')
custom_logger_file.critical('Це повідомлення рівня CRITICAL')