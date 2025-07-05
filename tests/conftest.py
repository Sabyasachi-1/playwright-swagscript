import os
#from operator import truediv

import pytest
from playwright.sync_api import sync_playwright, Page

#from Playwright.Test01 import browser

#Load environment variables from .env file ONLY if not in CI
if not os.getenv("CI"):
    from dotenv import load_dotenv
    load_dotenv()

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