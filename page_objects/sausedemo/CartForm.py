from playwright.sync_api import Locator, Page, expect


class CartForm:

    CART_LINK = "a.shopping_cart_link"
    CART_FORM_INDEX = "span.shopping_cart_badge"
    CART_TITLE = ".title"

    def __init__(self, page: Page):
        self.page = page

    @property
    def cart_form_index(self) -> int:
        cart_form_index: Locator = self.page.locator(self.__class__.CART_FORM_INDEX)
        text: str = cart_form_index.text_content()
        return int(text)

    def open(self):
        self.page.locator(self.__class__.CART_LINK).click()
        expect(self.page.locator(self.__class__.CART_TITLE)).to_be_visible()

    def count_items_in_cart(self) -> int:
        all_cart_items: list[Locator] = self.page.locator(".cart_item").all()
        return len(all_cart_items)

