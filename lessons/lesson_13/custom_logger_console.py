import logging
# Створення логера
custom_logger_console = logging.getLogger("custom_logger_console")

# Налаштування рівня логування
custom_logger_console.setLevel(logging.DEBUG)
#
# Створення обробника для запису в файл
console_handler = logging.StreamHandler()

# Налаштування рівня логування для обробника
console_handler.setLevel(logging.WARNING)

# Створення форматера для обробника
formatter = logging.Formatter('%(levelname)s - %(message)s')

console_handler.setFormatter(formatter)

# Додавання обробника до логера
custom_logger_console.addHandler(console_handler)

# Логування подій
custom_logger_console.debug('Це повідомлення рівня DEBUG')
custom_logger_console.info('Це повідомлення рівня INFO')
custom_logger_console.warning('Це повідомлення рівня WARNING')
custom_logger_console.error('Це повідомлення рівня ERROR')
custom_logger_console.critical('Це повідомлення рівня CRITICAL')