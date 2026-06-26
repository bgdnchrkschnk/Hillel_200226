import os

import allure
from playwright.sync_api import Page, Locator, expect
from dotenv import load_dotenv

from page_objects.sausedemo.ProductsPage import ProductsPage

load_dotenv()


class LoginPage:

    ENDPOINT = "/"
    USERNAME_FIELD = "#user-name"
    PASSWORD_FIELD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_BANNER = ".error>h3"

    def __init__(self, page: Page):
        self.page = page
        self.url = os.getenv("SAUSEDEMO_BASE_URL")+self.ENDPOINT

    @property
    def username_field(self) -> Locator:
        return self.page.locator(self.__class__.USERNAME_FIELD)

    @property
    def password_field(self) -> Locator:
        return self.page.locator(self.__class__.PASSWORD_FIELD)

    @property
    def login_button(self) -> Locator:
        return self.page.locator(self.__class__.LOGIN_BUTTON)

    @allure.step("Make sign in with username {username} and password {password}")
    def login(self, username: str, password: str, delay=100):
        self.username_field.type(text=username, delay=delay)
        self.password_field.type(text=password, delay=delay)
        self.login_button.click()
        return ProductsPage(self.page)

    @allure.step("Open sign in page")
    def open(self):
        if self.page.url != self.url:
            self.page.goto(self.url)

    @allure.step("Check error banner is visible")
    def expect_error_banner(self):
        expect(self.page.locator(self.__class__.ERROR_BANNER)).to_be_visible()
        expect(self.username_field).to_be_visible()
        expect(self.password_field).to_be_visible()
