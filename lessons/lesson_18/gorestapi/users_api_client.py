import requests

from lessons.lesson_18.gorestapi.base_api_client import BaseApiClient


class UsersApiClient(BaseApiClient):

    ENDPOINT = "users"

    def __init__(self):
        super().__init__()

    def create_user(self, test_user: dict) -> requests.Response:
        self.logger.info(f"Creating user: {test_user}")
        return self._post(endpoint=self.ENDPOINT, body=test_user)


