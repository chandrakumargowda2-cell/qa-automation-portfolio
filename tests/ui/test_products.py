import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
@pytest.mark.ui
@pytest.mark.smoke
def test_products_catalog_is_visible(page, base_url):
    home = HomePage(page); home.open(base_url); home.go_to_products()
    ProductsPage(page).verify_catalog()
@pytest.mark.ui
@pytest.mark.regression
def test_search_products_by_keyword(page, base_url):
    home = HomePage(page); home.open(base_url); home.go_to_products()
    products = ProductsPage(page); products.verify_catalog(); products.search("top"); products.verify_search_results()
