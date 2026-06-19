
from random import randint

from page_objects.sausedemo.ProductDetails import ProductDetails
from page_objects.sausedemo.ProductsPage import ProductsPage

class TestSauseDemoPositiveProducts:
    def test_product_is_opened(self, products_page_logged_standard_user: ProductsPage):
        random_placement = randint(1, 6)
        product_details: ProductDetails = products_page_logged_standard_user.open_product(placement=random_placement)
        assert product_details.is_page_opened(), f"ProductDetails page is not opened for product #{random_placement}"
