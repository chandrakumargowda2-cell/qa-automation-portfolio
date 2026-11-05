import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.data_factory import invalid_email
@pytest.mark.ui
@pytest.mark.negative
def test_login_rejects_invalid_credentials(page, base_url):
    home = HomePage(page); home.open(base_url); home.go_to_login()
    login = LoginPage(page); login.verify_form()
    login.login(invalid_email(), "WrongPassword_123!"); login.verify_invalid_login()
