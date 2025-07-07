from asyncio import timeout

from playwright.sync_api import Page, expect

class ProductPage:
    def __init__(self, page: Page):
        self.page=page
        self.sorting=page.locator('[data-test="product-sort-container"]')
        self.saucelabsfleecejacket=page.locator('[data-test="item-5-title-link"]').get_by_text('Sauce Labs Fleece Jacket')
        self.saucelabsbolttshirt=page.locator('[data-test="item-1-title-link"]').get_by_text("Sauce Labs Bolt T-Shirt")
        self.saucelabsbackpack=page.locator('[data-test="item-4-title-link"]').get_by_text('Sauce Labs Backpack')
        self.addtocart_from_productpage = page.locator('[data-test="add-to-cart"]')
        self.backtoproduct = page.locator('[data-test="back-to-products"]')

    def sort_items_lowtohigh(self):
        self.sorting.scroll_into_view_if_needed()
        expect(self.sorting).to_be_visible(timeout=20000)
        self.sorting.select_option('lohi')

    def sort_item_hightolow(self):
        self.sorting.scroll_into_view_if_needed()
        expect(self.sorting).to_be_visible(timeout=20000)
        self.sorting.select_option('hilo')

    def sauce_labs_fleece_jacket(self):
        self.saucelabsfleecejacket.click()
        self.addtocart_from_productpage.click()
        self.backtoproduct.click()

    def sauce_labs_bolt_tshirt(self):
        self.saucelabsbolttshirt.click()
        self.addtocart_from_productpage.click()
        self.backtoproduct.click()

    def sauce_labs_backpack(self):
        self.saucelabsbackpack.click()
        self.addtocart_from_productpage.click()
        self.backtoproduct.click()