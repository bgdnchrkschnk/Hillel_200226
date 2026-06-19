import os

from playwright.sync_api import Page, Locator, expect
from dotenv import load_dotenv
load_dotenv()


class ProductDetails:

    ENDPOINT = "/inventory-item.html?id="
    BACK_TO_PRODUCTS_PAGE_BUTTON = "#back-to-cart"
    ADD_TO_CART_BUTTON = "#add-to-cart"

    def __init__(self, page: Page):
        self.page = page
        self.url = os.getenv("SAUSEDEMO_BASE_URL") + self.ENDPOINT

    @property
    def back_to_products_page_button(self) -> Locator:
        return self.page.locator(self.__class__.BACK_TO_PRODUCTS_PAGE_BUTTON)

    @property
    def add_to_cart_button(self) -> Locator:
        return self.page.locator(self.__class__.ADD_TO_CART_BUTTON)


    def is_page_opened(self) -> bool:
        try:
            assert self.url in self.page.url  # .../inventory-item.html?id= in ... .../inventory-item.html?id=0
            expect(self.back_to_products_page_button).to_be_visible()
        except Exception:
            return False
        else:
            return True

