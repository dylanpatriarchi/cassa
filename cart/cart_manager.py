from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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
        user_input = input("Premi 'q' per stampare lo scontrino o qualsiasi altro tasto per continuare: ")
        if user_input.lower() == 'q':
            self.print_receipt()

    def print_receipt(self):
        filename = "scontrino.pdf"
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter

        c.drawString(100, height - 100, "Scontrino")
        c.drawString(100, height - 120, "="*30)

        y = height - 140
        for product in self.cart:
            c.drawString(100, y, f"Nome: {product['nome']} - Prezzo: €{product['prezzo']:.2f}")
            y -= 20

        total = sum(p['prezzo'] for p in self.cart)
        c.drawString(100, y, f"Totale: €{total:.2f}")

        c.save()
        print(f"Scontrino salvato in {filename}")