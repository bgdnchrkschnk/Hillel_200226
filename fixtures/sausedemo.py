import os
from dotenv import load_dotenv
load_dotenv()
import pytest

from page_objects.sausedemo.LoginPage import LoginPage


# @pytest.fixture
# def clear_page() -> Page:
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)  # headless - запуск без візуалу
#         page: Page = browser.new_page()
#         return page


@pytest.fixture
def login_page(page) -> LoginPage:
    lp: LoginPage = LoginPage(page)
    lp.open()
    return lp