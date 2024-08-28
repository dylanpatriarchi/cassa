from app import app
from barcode_scanner.scanner import start_scanner
from cart.cart_manager import CartManager

if __name__ == "__main__":
    cart_manager = CartManager()
    start_scanner(cart_manager)
    app.run(debug=True)