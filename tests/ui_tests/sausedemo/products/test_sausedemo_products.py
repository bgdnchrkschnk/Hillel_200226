
from random import randint

import allure
import pytest

from page_objects.sausedemo.ProductDetails import ProductDetails
from page_objects.sausedemo.ProductsPage import ProductsPage


@pytest.mark.regression
@allure.feature("Sausedemo Products")
class TestSauseDemoPositiveProducts:

    @allure.title("Test Products page is opened")
    # @allure.description("Test that user can open product details page")
    def test_product_is_opened(self, products_page_logged_standard_user: ProductsPage):
        """
        Test that user can open product details page
        """
        random_placement = randint(1, 6)
        product_details: ProductDetails = products_page_logged_standard_user.open_product(placement=random_placement)
        assert product_details.is_page_opened(), f"ProductDetails page is not opened for product #{random_placement}"
