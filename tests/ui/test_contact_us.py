
import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ui
def test_contact_us_page(page: Page, base_url):

    # Open application
    page.goto(base_url)

    # Click Contact Us
    page.get_by_role(
        "link", name="Contact us"
    ).click()

    # Verify navigation
    expect(page).to_have_url(
        re.compile(r".*/contact_us")
    )

    # Verify Contact Us heading
    expect(
        page.get_by_role("heading", name="GET IN TOUCH")
    ).to_be_visible()
