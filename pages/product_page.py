class ProductPage:
    def __init__(self, page):
        self.page = page

    def select_product(self, product_name):
        self.page.click(f"text={product_name}")
        self.page.wait_for_selector("h2.name")

    def add_to_cart(self):
        self.page.click("a.btn.btn-success.btn-lg")  # Add to cart button
        self.page.on("dialog", lambda dialog: dialog.accept())  # Accept alert
