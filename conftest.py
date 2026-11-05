from datetime import datetime
from pathlib import Path
import re
import pytest
import os
from playwright.sync_api import sync_playwright
from api.api_client import ApiClient
from config.settings import BASE_URL, BROWSER, DEFAULT_TIMEOUT, HEADLESS, SLOW_MO, IS_CI

for folder in ("reports", "screenshots", "traces"):
    Path(folder).mkdir(exist_ok=True)

def pytest_addoption(parser): parser.addoption("--app-url", action="store", default=BASE_URL)

def pytest_configure(config):
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    config.option.htmlpath = f"reports/report_{stamp}.html"
    config.option.self_contained_html = True

@pytest.fixture(scope="session")
def base_url(request): return request.config.getoption("--app-url").rstrip("/")

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p: yield p

@pytest.fixture
def browser_instance(playwright_instance):

    browser_name = os.getenv("BROWSER", BROWSER).lower()

    headless_value = os.getenv(
        "HEADLESS", str(HEADLESS)
    ).strip().lower()

    headless = headless_value not in (
        "false", "0", "no", "off"
    )

    browser_type = getattr(
        playwright_instance, browser_name
    )

    print(f"\nBrowser: {browser_name}")
    print(f"Headless mode: {headless}")

    browser = browser_type.launch(
        headless=headless,
        slow_mo=SLOW_MO
    )

    yield browser

    browser.close()

@pytest.fixture
def context(browser_instance):
    ctx = browser_instance.new_context(viewport={"width": 1440, "height": 900})
    ctx.set_default_timeout(DEFAULT_TIMEOUT)
    ctx.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield ctx
    try: ctx.tracing.stop()
    except Exception: pass
    ctx.close()

@pytest.fixture
def page(context): return context.new_page()

@pytest.fixture
def api_client():
    client = ApiClient(); yield client; client.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield; report = outcome.get_result()
    if report.when == "call" and report.failed:
        safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", item.nodeid)
        page_obj = item.funcargs.get("page"); ctx = item.funcargs.get("context")
        if page_obj:
            try: page_obj.screenshot(path=f"screenshots/{safe}.png", full_page=True)
            except Exception: pass
        if ctx:
            try: ctx.tracing.stop(path=f"traces/{safe}.zip")
            except Exception: pass
