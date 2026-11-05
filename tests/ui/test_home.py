import pytest
from pages.home_page import HomePage

@pytest.mark.ui
@pytest.mark.smoke
def test_home_page_loads(page, base_url):
    home = HomePage(page); home.open(base_url); home.verify_loaded()
