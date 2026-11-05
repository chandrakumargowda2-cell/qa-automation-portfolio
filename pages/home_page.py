import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.logo = page.locator("a[href='/'] img").first
        self.products_link = page.locator("a[href='/products']").first
        self.login_link = page.locator("a[href='/login']").first
    def verify_loaded(self):
        expect(self.page).to_have_title(re.compile("Automation", re.IGNORECASE))
        expect(self.logo).to_be_visible()
    def go_to_products(self): self.products_link.click()
    def go_to_login(self): self.login_link.click()
