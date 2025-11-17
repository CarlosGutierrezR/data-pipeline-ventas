import psycopg2

def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        user="admin",
        password="admin123",
        dbname="ventasdb"
    )
    return connection

if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Conexión exitosa a PostgreSQL 🚀")
        conn.close()
    except Exception as e:
        print("Error de conexión:", e)
