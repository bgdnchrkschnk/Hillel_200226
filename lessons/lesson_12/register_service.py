import logging
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
    if "@" not in email or email.count("@") > 1:
        return {"success": False, "status_code": 400, "error": "Email is not valid"}

    if not phone.isdigit():
        return {"success": False, "status_code": 400, "error": "Phone is not valid"}

    if len(password) < 6 or (password.lower() == password):
        return {"success": False, "status_code": 400, "error": "Password is too short"}

    if username in REGISTERED_USERS:
        raise RegistrationServiceError("User is already registered")

    logger.info(f"User {username} registered successfully")

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
    print(sys.path)
