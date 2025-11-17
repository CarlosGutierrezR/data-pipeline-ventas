import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from conexion_postgres import get_connection

def obtener_df(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def generar_dashboard():

    # 1. Ventas por día
    df_diario = obtener_df("""
        SELECT DATE(fecha_orden) AS fecha, SUM(total) AS ventas
        FROM ordenes
        GROUP BY DATE(fecha_orden)
        ORDER BY fecha;
    """)

    plt.figure(figsize=(10,5))
    plt.plot(df_diario["fecha"], df_diario["ventas"], marker="o")
    plt.title("Ventas por día")
    plt.xlabel("Fecha")
    plt.ylabel("Ventas")
    plt.grid()
    plt.tight_layout()
    plt.savefig("../reports/ventas_por_dia.png")
    plt.close()

    # 2. Top productos
    df_top = obtener_df("""
        SELECT p.nombre, SUM(d.cantidad) AS unidades
        FROM detalle_ordenes d
        JOIN productos p ON p.id_producto = d.id_producto
        GROUP BY p.nombre
        ORDER BY unidades DESC
        LIMIT 10;
    """)

    fig = px.bar(df_top, x="nombre", y="unidades", title="Top Productos")
    fig.write_image("../reports/top_productos.png")

    # 3. Top clientes
    df_clientes = obtener_df("""
        SELECT c.nombre, COUNT(o.id_orden) AS ordenes
        FROM ordenes o
        JOIN clientes c ON c.id_cliente = o.id_cliente
        GROUP BY c.nombre
        ORDER BY ordenes DESC
        LIMIT 10;
    """)

    fig2 = px.bar(df_clientes, x="ordenes", y="nombre",
                  orientation="h", title="Top Clientes")
    fig2.write_image("../reports/top_clientes.png")

    print("Dashboards generados en /reports correctamente 🚀")

if __name__ == "__main__":
    generar_dashboard()
