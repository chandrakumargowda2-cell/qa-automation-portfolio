from playwright.sync_api import Page, expect
from pages.base_page import BasePage
class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email = page.locator("input[data-qa='login-email']")
        self.password = page.locator("input[data-qa='login-password']")
        self.submit = page.locator("button[data-qa='login-button']")
        self.heading = page.get_by_text("Login to your account", exact=True)
        self.error = page.get_by_text("Your email or password is incorrect!", exact=True)
    def verify_form(self):
        expect(self.heading).to_be_visible(); expect(self.email).to_be_visible(); expect(self.password).to_be_visible()
    def login(self, email, password):
        self.email.fill(email); self.password.fill(password); self.submit.click()
    def verify_invalid_login(self): expect(self.error).to_be_visible()
