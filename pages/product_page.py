from playwright.sync_api import Page, expect

class ProductPage:
    def __init__(self, page: Page):
        self.page=page
        self.sorting=page.locator('[data-test="product-sort-container"]')
    def sort_items_lowtohigh(self):

        self.sorting.scroll_into_view_if_needed()
        expect(self.sorting).to_be_visible(timeout=20000)
        self.sorting.select_option('lohi')