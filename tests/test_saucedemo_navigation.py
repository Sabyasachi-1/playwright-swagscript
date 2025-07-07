from playwright.sync_api import expect, Page
import pytest

from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage

def test_saucedemo_navigation(page: Page, username, password):
    login_page = LoginPage(page)
    checkout_page = CheckoutPage(page)
    product_page = ProductPage(page)

    login_page.navigate()
    login_page.login(username, password)
    expect(page.get_by_text('Swag Labs')).to_be_visible()
    page.wait_for_load_state('networkidle')

    product_page.sort_item_hightolow()
    product_page.sauce_labs_fleece_jacket()

    product_page.sort_item_hightolow()
    product_page.sauce_labs_bolt_tshirt()

    product_page.sort_item_hightolow()
    product_page.sauce_labs_backpack()

    page.locator('[data-test="remove-sauce-labs-bolt-t-shirt"]').click()

    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("2")
    page.locator('[data-test="shopping-cart-link"]').click()

    # Navigate to Cart and fill information
    page.locator('[data-test="checkout"]').click()
    checkout_page.Fill_your_Information('Sabya', 'TestQA', '54601')

    # Complete Checkout
    checkout_page.finish_order()
    checkout_page.verify_checkout_complete()
