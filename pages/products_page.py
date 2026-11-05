from playwright.sync_api import Page, expect
from pages.base_page import BasePage
class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.heading = page.get_by_role("heading", name="All Products")
        self.search_input = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")
        self.searched_heading = page.get_by_role("heading", name="Searched Products")
        self.cards = page.locator(".product-image-wrapper")
    def verify_catalog(self):
        expect(self.heading).to_be_visible(); expect(self.cards.first).to_be_visible()
    def search(self, keyword):
        self.search_input.fill(keyword); self.search_button.click()
    def verify_search_results(self):
        expect(self.searched_heading).to_be_visible(); expect(self.cards.first).to_be_visible()
