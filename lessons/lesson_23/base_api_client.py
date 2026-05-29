import os

import requests
from requests import Session, Response

from lessons.lesson_23.abstract_api_client import AbstractQAAutoAPIClient
from dotenv import load_dotenv

from lessons.lesson_23.data_models.sign_up_response_model import SignUpResponseModel
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()


class BaseQAAutoAPIClient(AbstractQAAutoAPIClient):

    BASE_URL = os.getenv("QAUTO_API_BASE_URL")

    def __init__(self):
        self.session: Session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"}) # буде у всіх наших реквестах

    def _get(self, endpoint: str) -> Response:
        final_url = self.BASE_URL + endpoint
        return self.session.get(url=final_url)

    def _post(self, endpoint: str, data: dict) -> Response:
        final_url = self.BASE_URL + endpoint
        # return self.session.post(url=final_url, data=data) # data=json.dumps(data)
        return self.session.post(url=final_url, json=data) # dict -> json ( json.dumps(data) )

    def sign_up(self, request_data: dict) -> Response:
        final_url = self.BASE_URL + "/auth/signup"
        response: Response = self._post(endpoint=final_url, data=request_data)
        response_dict: dict = response.json() # json.loads(response.text)
        SignUpResponseModel.model_validate(**response_dict)
        return response

    def sign_in(self, email: str, password: str, remember=False) -> Response:
        final_url = self.BASE_URL + "/auth/signin"
        sign_in_request = {"email": email, "password": password, "remember": remember}
        return self._post(endpoint=final_url, data=sign_in_request)

    def log_out(self) -> Response:
        final_url = self.BASE_URL + "/auth/logout"
        return self._get(endpoint=final_url)




# def test_sign_up():
#     sign_up_data = get_sign_up_request()
#     response = client.sign_up(request_data=sign_up_data)
#     response = client.sign_in(email=sign_up_data["email"], password=sign_up_data["password"])


# def test_reset_pw():
    # client = APIClient()
    # webdriver = playwright()
    # client.log_out()

    # webdriver.open_email_inbox()
    # assert webdriver.find_new_reset_pw_mail()


# def test_with_clear_db():
#     try:
#         api_client = BaseQAAutoAPIClient()
#         db_client = BaseQAAutoAPIClient()
#         api_client.sign_up()
#         api_client.sign_in()
#         api_client.log_out()
#     finally:
#         # post_condiiton
#         db_client.clear_test_data_for_today()

