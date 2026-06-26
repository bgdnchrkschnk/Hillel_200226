import os
import time
from random import randint

import allure
import pytest
from dotenv import load_dotenv


load_dotenv()

@pytest.mark.regression
@allure.feature("Sausedemo Cart")
class TestSauceDemoPositiveCart:


    @pytest.mark.parametrize("count_of_clicked_products", [
        1, 6, randint(2, 6)
    ])
    @allure.title("Test added products count in cart icon")
    def test_products_count_cart_in_icon(self, products_page_logged_standard_user, count_of_clicked_products):
        """
        Test that user can add products to cart
        """
        if count_of_clicked_products == 1:
            products_page_logged_standard_user.add_product_to_cart(placement=randint(1, 6))
        else:
            for placement in range(count_of_clicked_products):
                products_page_logged_standard_user.add_product_to_cart(placement=placement)
        with allure.step("Check that cart icon has correct count of products"):
            assert products_page_logged_standard_user.cart_form.cart_form_index == count_of_clicked_products

    @allure.title("Test added products count in cart")
    def test_products_count_in_cart(self, products_page_logged_standard_user):
        """
        Test that user can add products to cart
        """
        random_placement = randint(1, 6)
        products_page_logged_standard_user.add_product_to_cart(placement=random_placement)
        products_page_logged_standard_user.cart_form.open()
        with allure.step("Check that cart has correct count of products"):
            assert products_page_logged_standard_user.cart_form._count_items_in_cart() == 1
