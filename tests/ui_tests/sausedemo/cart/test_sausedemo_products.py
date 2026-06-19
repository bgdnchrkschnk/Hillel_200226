import os
import time
from random import randint

import pytest
from playwright.sync_api import sync_playwright, Locator, expect, Page
from dotenv import load_dotenv

from page_objects.sausedemo.LoginPage import LoginPage
from page_objects.sausedemo.ProductDetails import ProductDetails
from page_objects.sausedemo.ProductsPage import ProductsPage

load_dotenv()

class TestSauceDemoPositiveCart:


    @pytest.mark.parametrize("count_of_clicked_products", [
        1, 6, randint(2, 6)
    ])
    def test_products_count_cart_in_icon(self, products_page_logged_standard_user, count_of_clicked_products):

        if count_of_clicked_products == 1:
            products_page_logged_standard_user.add_product_to_cart(placement=randint(1, 6))
        else:
            for placement in range(count_of_clicked_products):
                products_page_logged_standard_user.add_product_to_cart(placement=placement)
        assert products_page_logged_standard_user.cart_form.cart_form_index == count_of_clicked_products

    def test_products_count_in_cart(self, products_page_logged_standard_user):
        random_placement = randint(1, 6)
        products_page_logged_standard_user.add_product_to_cart(placement=random_placement)
        time.sleep(2)
        products_page_logged_standard_user.cart_form.open()
        time.sleep(2)
        assert products_page_logged_standard_user.cart_form.count_items_in_cart() == 1



    # trace viewer

    # test+ return page class
    # slowmo