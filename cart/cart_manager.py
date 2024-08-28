class CartManager:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)
        self.show_cart()

    def remove_product(self, product_id):
        self.cart = [p for p in self.cart if p['id'] != product_id]
        self.show_cart()

    def show_cart(self):
        total = sum(p['prezzo'] for p in self.cart)
        print(f"Carrello: {[p['nome'] for p in self.cart]}")
        print(f"Totale: €{total}")
