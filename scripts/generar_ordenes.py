import random
from faker import Faker
import psycopg2
from conexion_postgres import get_connection

fake = Faker()

def generar_ordenes(n_ordenes=30):
    conn = get_connection()
    cur = conn.cursor()

    # Obtener clientes existentes
    cur.execute("SELECT id_cliente FROM clientes")
    clientes = [row[0] for row in cur.fetchall()]

    # Obtener productos existentes
    cur.execute("SELECT id_producto, precio FROM productos")
    productos = cur.fetchall()  # (id_producto, precio)

    for _ in range(n_ordenes):

        # ------- CREAR ORDEN -------
        id_cliente = random.choice(clientes)

        cur.execute("""
            INSERT INTO ordenes (id_cliente, estado)
            VALUES (%s, 'CREADA')
            RETURNING id_orden
        """, (id_cliente,))
        
        id_orden = cur.fetchone()[0]

        # ------- CREAR DETALLE -------
        num_items = random.randint(1, 4)  # entre 1 y 4 productos por orden
        total_orden = 0

        for _ in range(num_items):
            prod = random.choice(productos)
            id_producto, precio = prod

            cantidad = random.randint(1, 3)
            subtotal = precio * cantidad
            total_orden += subtotal

            cur.execute("""
                INSERT INTO detalle_ordenes (id_orden, id_producto, cantidad, precio_unitario, subtotal)
                VALUES (%s, %s, %s, %s, %s)
            """, (id_orden, id_producto, cantidad, precio, subtotal))

        # ------- ACTUALIZAR TOTAL DE LA ORDEN -------
        cur.execute("""
            UPDATE ordenes
            SET total = %s
            WHERE id_orden = %s
        """, (total_orden, id_orden))

    conn.commit()
    cur.close()
    conn.close()

    print(f"{n_ordenes} órdenes generadas correctamente 🚀")

if __name__ == "__main__":
    generar_ordenes(30)
