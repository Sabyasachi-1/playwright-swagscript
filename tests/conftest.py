#Load environment variables from .env file ONLY if not in CI
from dotenv import load_dotenv
load_dotenv()

import os
#from operator import truediv

import pytest
from playwright.sync_api import sync_playwright, Page
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
#Only take screenshot if test failed during execution
    if report.when == 'call' and report.failed:
        page = item.funcargs.get('page',None)
        if page:
            screenshot_path = f"screenshot_{item.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"\n Screenshot captured: {screenshot_path}")
#from Playwright.Test01 import browser



# Fixtures for Credentials
@pytest.fixture(scope="session")
def username() -> str:
    return os.getenv("SWAG_USERNAME")
@pytest.fixture(scope='session')
def password() -> str:
    return os.getenv("SWAG_PASSWORD")

#Fixtures for Playwright
@pytest.fixture(scope="function")
def page():
    HEADLESS = os.getenv("CI", "false").lower()== "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        context = browser.new_context(viewport=None)
        page = context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()