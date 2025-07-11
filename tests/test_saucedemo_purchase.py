from playwright.sync_api import sync_playwright, expect, Page
import pytest

#
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage

#---Testcases---
def test_saucedemo_successfull_purchase(page: Page, username, password):
        login_page = LoginPage(page)
        checkout_page = CheckoutPage(page)
        product_page = ProductPage(page)
#Login
        login_page.navigate()
        login_page.login(username, password)
        expect(page.get_by_text('Swag Labs')).to_be_visible()
        page.wait_for_load_state('networkidle')
        #Add items to cart
        product_page.sort_items_lowtohigh()
        page.locator('[data-test="add-to-cart-sauce-labs-onesie"]').click()
        page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
        expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("2")
        page.locator('[data-test="shopping-cart-link"]').click()
#Navigate to Cart and fill information
        page.locator('[data-test="checkout"]').click()
        checkout_page.Fill_your_Information('Sabya','TestQA','54601')

#Complete Checkout
        checkout_page.finish_order()
        checkout_page.verify_checkout_complete()


# CI TRIGGER 010


