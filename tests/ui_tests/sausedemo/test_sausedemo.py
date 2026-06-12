import os

from playwright.sync_api import sync_playwright, Locator, expect, Page
from dotenv import load_dotenv

from page_objects.sausedemo.LoginPage import LoginPage
from page_objects.sausedemo.ProductsPage import ProductsPage

load_dotenv()


class TestSauseDemoAuthorization:

    def test_sausedemo_login_is_successful(self, login_page: LoginPage):
        products_page: ProductsPage = login_page.login(
            username=os.getenv("SAUSEDEMO_STANDART_USERNAME"),
            password=os.getenv("SAUSEDEMO_PASSWORD"), delay=300
        )
        assert products_page.is_logged_in()


    def test_sausedemo_login_is_failed_locked_user(self, login_page: LoginPage):
        login_page.login(username=os.getenv("SAUSEDEMO_LOCKED_USERNAME"),
                         password=os.getenv("SAUSEDEMO_PASSWORD"))
        login_page.expect_error_banner()
