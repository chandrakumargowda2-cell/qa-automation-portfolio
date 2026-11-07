
import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ui
def test_test_cases_page(page: Page, base_url):

    # Open application
    page.goto(base_url)

    # Click Test Cases
    page.get_by_role(
        "link", name="Test Cases"
    ).first.click()

    # Verify navigation
    expect(page).to_have_url(
        re.compile(r".*/test_cases")
    )

    # Verify Test Cases heading
    expect(
        page.locator("h2.title")
    ).to_contain_text("Test Cases")
