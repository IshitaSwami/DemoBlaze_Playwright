class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_link = page.locator("#cartur")
        self.place_order_button = page.locator("button[data-target='#orderModal']")

    def go_to_cart(self):
        self.cart_link.click()

    def place_order(self):
        self.place_order_button.click()

    def fill_order_form(self, name, country, city, card, month, year):
        self.page.fill("#name", name)
        self.page.fill("#country", country)
        self.page.fill("#city", city)
        self.page.fill("#card", card)
        self.page.fill("#month", month)
        self.page.fill("#year", year)
        self.page.click("button[onclick='purchaseOrder()']")

    def confirm_order(self):
        self.page.wait_for_selector("div.sweet-alert")  # Confirmation modal
        return self.page.inner_text("div.sweet-alert")
