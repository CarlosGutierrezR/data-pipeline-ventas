from faker import Faker
import psycopg2
from conexion_postgres import get_connection

fake = Faker()

def insertar_clientes(n=20):
    conn = get_connection()
    cur = conn.cursor()

    sql = """
        INSERT INTO clientes (nombre, email, pais, ciudad)
        VALUES (%s, %s, %s, %s)
    """

    for _ in range(n):
        nombre = fake.name()
        email = fake.unique.email()
        pais = fake.country()
        ciudad = fake.city()

        cur.execute(sql, (nombre, email, pais, ciudad))

    conn.commit()
    cur.close()
    conn.close()
    print(f"{n} clientes insertados correctamente 🚀")

if __name__ == "__main__":
    insertar_clientes(20)
