import time
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_place_order(page):
    home = HomePage(page)
    product = ProductPage(page)
    cart = CartPage(page)

    # Go to site and login
    home.goto()
    home.login("testuser", "testpass")  # Dummy login; might need to register first

    # Select product and add to cart
    product.select_product("Samsung galaxy s6")
    product.add_to_cart()
    page.wait_for_timeout(2000)

    # Go to cart and place order
    cart.go_to_cart()
    page.wait_for_timeout(2000)
    cart.place_order()
    cart.fill_order_form("John Doe", "USA", "NYC", "123456789", "12", "2025")

    confirmation_text = cart.confirm_order()
    assert "Thank you for your purchase!" in confirmation_text
