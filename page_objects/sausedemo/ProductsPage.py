import os
from csv import excel

from dotenv import load_dotenv
load_dotenv()
from playwright.sync_api import Page, Locator, expect


class ProductsPage:

    ENDPOINT = "/inventory.html"
    PRODUCTS_TITLE = ".title"
    CART = "a[data-test=shopping-cart-link]"

    def __init__(self, page: Page):
        self.page = page
        self.url = os.getenv("SAUSEDEMO_BASE_URL")+self.ENDPOINT

    def open_product(self, placement: int):
        all_products: list[Locator] = self.page.locator("div.inventory_item_label a").all() # expected count - 6
        all_products[placement-1].click()


    def is_logged_in(self) -> bool:

        try:
            expect(self.page).to_have_url(self.url)
            expect(self.page.locator(self.__class__.PRODUCTS_TITLE)).to_be_visible()
            expect(self.page.locator(self.__class__.PRODUCTS_TITLE)).to_have_text("Products")
            expect(self.page.locator(self.__class__.CART)).to_be_visible()
            return True
        except Exception as e:
            return False


