import cv2
from pyzbar.pyzbar import decode
from app.utils import get_db_connection

def get_product_by_barcode(barcode):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM prodotti WHERE codice_barre = %s"
    cursor.execute(query, (barcode,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()
    return product

def start_scanner(cart_manager):
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        for barcode in decode(frame):
            barcode_data = barcode.data.decode('utf-8')
            product = get_product_by_barcode(barcode_data)
            if product:
                cart_manager.add_product(product)
                print(f"Aggiunto al carrello: {product['nome']} - €{product['prezzo']}")
            else:
                print("Prodotto non trovato.")

            cv2.rectangle(frame, (barcode.rect.left, barcode.rect.top), 
                          (barcode.rect.left + barcode.rect.width, barcode.rect.top + barcode.rect.height), 
                          (0, 255, 0), 2)
            cv2.putText(frame, barcode_data, (barcode.rect.left, barcode.rect.top - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        cv2.imshow("Codice a barre", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()