from dotenv import load_dotenv
import os
load_dotenv()
USERNAME = os.getenv("SWAG_USERNAME")
PASSWORD = os.getenv("SWAG_PASSWORD")

from playwright.sync_api import sync_playwright, expect
run_headless = os.getenv("CI", "false").lower()=="true"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport=None)
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")
    #login
    page.locator('[data-test="username"]').fill(USERNAME)
    page.locator('[data-test="password"]').fill(PASSWORD)
    page.locator('[data-test="login-button"]').click()

    expect(page.get_by_text('Swag Labs')).to_be_visible()
    page.locator('[data-test="product-sort-container"]').select_option('lohi')
    page.locator('[data-test="add-to-cart-sauce-labs-onesie"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("2")
    page.locator('[data-test="shopping-cart-link"]').click()
    page.locator('[data-test="checkout"]').click()
    page.locator('[data-test="firstName"]').fill('Sabya')
    page.locator('[data-test="lastName"]').fill('Test')
    page.locator('[data-test="postalCode"]').fill('00111')
    page.locator('[data-test="continue"]').click()
    page.locator('[data-test="finish"]').click()
    expect(page.locator('[data-test="complete-header"]')).to_have_text("Thank you for your order!")

#CI TRIGGER02



