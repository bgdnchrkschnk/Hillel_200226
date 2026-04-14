from lessons.lesson_13.custom_logger_full import custom_logger_full

def is_adult(age):
    custom_logger_full.info(f"Checking age: {age}")
    return age >= 18

