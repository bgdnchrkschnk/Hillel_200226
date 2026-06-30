import os

import pytest
import allure
from dotenv import load_dotenv

from page_objects.sausedemo.LoginPage import LoginPage
from page_objects.sausedemo.ProductsPage import ProductsPage

load_dotenv()

@pytest.mark.regression
@allure.feature("Sausedemo Authorization")
class TestSauseDemoPositiveAuthorization:
    """
    Test suite related to authorization functionalities
    """
    @allure.title("Login is successful")
    @allure.link(url="https://www.saucedemo.com/", name="SauseDemo")
    @allure.issue(url="https://github.com/qauto/qauto_automation_framework/issues/1", name="Login is not working")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_sausedemo_login_is_successful(self, login_page: LoginPage):
        """
        Test that user can login to SauseDemo
        """
        products_page: ProductsPage = login_page.login(
            username=os.getenv("SAUSEDEMO_STANDART_USERNAME"),
            password=os.getenv("SAUSEDEMO_PASSWORD"), delay=20
        )
        assert products_page.is_logged_in()

@pytest.mark.regression
@allure.feature("Sausedemo Authorization")
class TestSauseDemoNegativeAuthorization:

    @allure.title("Login is failed with locked user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sausedemo_login_is_failed_locked_user(self, login_page: LoginPage):
        """
        Test that user can't login to SauseDemo with locked user
        """
        login_page.login(username=os.getenv("SAUSEDEMO_LOCKED_USERNAME"),
                         password=os.getenv("SAUSEDEMO_PASSWORD"))
        login_page.expect_error_banner()