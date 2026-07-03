# import os
# import unittest
# import requests
# from dotenv import load_dotenv
#
# # from lessons.lesson_18.user_provider import get_test_user
# from lessons.lesson_18.gorestapi.users_api_client import UsersApiClient
#
# load_dotenv()
#
# class TestGorestUsers(unittest.TestCase):
#
#     API_TOKEN = os.getenv("API_TOKEN")
#     ENDPOINT = os.getenv("BASE_URL") + "/users"
#
#     def test_user_creation(self, logging_test_precondition):
#         headers = {
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {self.API_TOKEN}"
#         }
#
#
#         test_user_data: dict = get_test_user()
#
#         response: requests.Response = requests.post(url=self.ENDPOINT, json=test_user_data, headers=headers)
#         response_dict: dict = response.json() # json.loads(response.text)
#         assert response.ok == True, f"Expected status_code 201, but got {response.status_code}"
#         assert test_user_data.items() <= response_dict.items() # перевірка що відправлений юзер є в респонсі
#         assert "id" in response_dict.keys()
#         assert response_dict.get("id") is not None
#
#     def test_get_user_by_id(self):
#         user_api_client = UsersApiClient()
#         test_user_data: dict = get_test_user()
#
#         response = user_api_client.create_user(test_user=test_user_data)
#         assert response.ok == True, f"Expected status_code 201, but got {response.status_code}"
#
#         ...