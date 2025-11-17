import pandas as pd
import psycopg2
from conexion_postgres import get_connection

def obtener_df(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def analisis_basico():

    # Total ventas
    df_ventas = obtener_df("SELECT SUM(total) AS ventas_totales FROM ordenes;")
    print("💰 Ventas Totales:", df_ventas.iloc[0,0])

    # Top 5 productos
    df_top_prod = obtener_df("""
        SELECT p.nombre, SUM(d.cantidad) AS unidades_vendidas
        FROM detalle_ordenes d
        JOIN productos p ON p.id_producto = d.id_producto
        GROUP BY p.nombre
        ORDER BY unidades_vendidas DESC
        LIMIT 5;
    """)
    print("\n🏆 Top 5 Productos más vendidos:")
    print(df_top_prod)

    # Top clientes
    df_top_clientes = obtener_df("""
        SELECT c.nombre, COUNT(o.id_orden) AS ordenes
        FROM ordenes o
        JOIN clientes c ON c.id_cliente = o.id_cliente
        GROUP BY c.nombre
        ORDER BY ordenes DESC
        LIMIT 5;
    """)
    print("\n🧑‍💼 Clientes con más compras:")
    print(df_top_clientes)

if __name__ == "__main__":
    analisis_basico()
