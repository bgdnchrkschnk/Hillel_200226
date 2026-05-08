import os
import requests
from dotenv import load_dotenv

from lessons.lesson_13.custom_logger_full import custom_logger_full

load_dotenv()


class BaseApiClient:

    BASE_URL = os.getenv("BASE_URL")

    def __init__(self):
        self.api_token = os.getenv("API_TOKEN")
        self.session = requests.Session()
        self.authentificate()
        self.logger = custom_logger_full

    def authentificate(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_token}"
        }

        self.session.headers.update(headers)

    def _get(self, endpoint) -> requests.Response:
        return self.session.get(f"{self.BASE_URL}{endpoint}")

    def _post(self, endpoint, body) -> requests.Response:
        self.logger.info(f"Sending request to {self.BASE_URL}{endpoint} with body: {body}, headers: {self.session.headers}")
        return self.session.post(f"{self.BASE_URL}{endpoint}", json=body, timeout=10)


    # FIXME: fix this method
    def _put(self, endpoint) -> requests.Response:
        return self.session.get(f"{self.BASE_URL}{endpoint}")

    def _delete(self, endpoint) -> requests.Response:
        return self.session.get(f"{self.BASE_URL}{endpoint}")