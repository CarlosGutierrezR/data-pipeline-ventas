import requests
import psycopg2
from conexion_postgres import get_connection

URL = "https://fakestoreapi.com/products"

def etl_productos():
    print("Extrayendo productos desde API...")
    response = requests.get(URL)

    if response.status_code != 200:
        print("Error al obtener datos:", response.status_code)
        return

    productos = response.json()

    conn = get_connection()
    cur = conn.cursor()

    sql = """
        INSERT INTO productos (nombre, categoria, precio, stock, activo)
        VALUES (%s, %s, %s, %s, TRUE)
    """

    for p in productos:
        nombre = p["title"]
        categoria = p["category"]
        precio = float(p["price"])
        stock = 50  # valor inicial realista

        cur.execute(sql, (nombre, categoria, precio, stock))

    conn.commit()
    cur.close()
    conn.close()
    print(f"{len(productos)} productos cargados correctamente 🚀")

if __name__ == "__main__":
    etl_productos()
