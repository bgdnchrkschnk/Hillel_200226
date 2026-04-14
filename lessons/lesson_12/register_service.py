from lessons.lesson_13.custom_logger_full import custom_logger_full
import sys

class RegistrationServiceError(Exception):
    ...


REGISTERED_USERS = ["registered_user"]

def register_user(username: str,
                  password: str,
                  email: str,
                  phone: str):
    """
    The function to register user
    """
    custom_logger_full.info(f"Trying to register user with username={username}")
    if "@" not in email or email.count("@") > 1:
        custom_logger_full.error(f"Email {email} is not valid")
        return {"success": False, "status_code": 400, "error": "Email is not valid"}

    if not phone.isdigit():
        custom_logger_full.error(f"Phone number {phone} is not valid")
        return {"success": False, "status_code": 400, "error": "Phone is not valid"}

    if len(password) < 6 or (password.lower() == password):
        custom_logger_full.error(f"Password {password} is too short")
        return {"success": False, "status_code": 400, "error": "Password is too short"}

    if username in REGISTERED_USERS:
        custom_logger_full.warning(f"User {username} is already registered!")
        raise RegistrationServiceError("User is already registered")

    custom_logger_full.info(f"User {username} registered successfully")

    return {
        "success": True,
        "status_code": 200,
        "user": {
            "username": username,
            "email": email,
            "phone": phone
        }
    }


if __name__ == "__main__": # якщо запуск з цього файлу то виконай це (якщо цей файл імпортується то не виконуй наступний код)
    print(
        register_user("Ivan", "bfjhebjhsF", "ivantester@gmail.com", "727867394")
    )
