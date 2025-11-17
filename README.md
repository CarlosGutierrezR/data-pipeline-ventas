📌 Proyecto: Data Pipeline de Ventas

Este proyecto implementa un pipeline completo y automatizado de procesamiento de datos de ventas, utilizando una arquitectura moderna basada en:

🐘 PostgreSQL (almacenamiento)

🐍 Python (ETL, análisis, reportes)

🐳 Docker & Docker Compose (contenedorización)

🌬️ Apache Airflow 2.6.3 (orquestación)

📊 Plotly / Matplotlib (visualización de datos)

El objetivo principal es simular un flujo real de datos corporativos, procesarlos y generar reportes diarios, totalmente automatizados por Airflow.

🧱 Arquitectura del Pipeline
            ┌────────────────────────┐
            │     Datos Iniciales     │
            │ (clientes / productos)  │
            └────────────┬────────────┘
                         ↓
               ┌─────────────────┐
               │ Generar Órdenes │
               └───────┬─────────┘
                       ↓
              ┌──────────────────┐
              │ ETL a PostgreSQL │
              └───────┬──────────┘
                      ↓
       ┌──────────────────────────────┐
       │ Análisis y KPI de Ventas     │
       └───────┬──────────────────────┘
               ↓
     ┌───────────────────────────────┐
     │ Dashboards (PNG automáticos)  │
     └───────────────────────────────┘


Todo el flujo está orquestado por Airflow en un DAG llamado pipeline_ventas.

📂 Estructura del Proyecto
data-pipeline-ventas/
│
├── airflow/
│   └── dags/
│       └── pipeline_ventas.py
│
├── data/
│   ├── clientes.csv
│   ├── productos.csv
│   └── ordenes.csv
│
├── docker/
│   ├── docker-compose.yml
│   ├── docker-compose-airflow.yml
│   └── README_docker.md
│
├── reports/
│   ├── top_clientes.png
│   ├── top_productos.png
│   └── ventas_por_dia.png
│
├── scripts/
│   ├── analisis_ventas.py
│   ├── conexion_postgres.py
│   ├── dashboard_ventas.py
│   ├── etl_productos.py
│   ├── generar_ordenes.py
│   └── insertar_clientes.py
│
├── README.md
└── requirements.txt

⚙️ Tecnologías
Componente	Descripción
Airflow 2.6.3	Orquestación del pipeline
PostgreSQL 13	Base de datos
Python 3.10+	Scripts ETL, análisis, dashboards
Docker Compose	Contenedorización completa
Plotly / Matplotlib	Dashboards automáticos
🚀 Cómo ejecutar el proyecto
1️⃣ Clonar el repositorio
git clone https://github.com/CarlosGutierrezR/data-pipeline-ventas.git
cd data-pipeline-ventas

2️⃣ Levantar los servicios con Docker

Entrar en la carpeta docker:

cd docker


Levantar Airflow, Redis y PostgreSQL:

docker compose -f docker-compose-airflow.yml up -d


Airflow estará disponible en:

👉 http://localhost:8081

3️⃣ Credenciales de acceso a Airflow
Usuario	Contraseña
airflow	airflow
4️⃣ Ejecutar el pipeline

En Airflow:

➡️ Busca el DAG: pipeline_ventas
➡️ Actívalo
➡️ Haz clic en Trigger DAG

Esto ejecutará automáticamente todos los scripts del pipeline:

✔ Inserción de clientes
✔ Inserción de productos
✔ Generación de órdenes
✔ ETL hacia PostgreSQL
✔ Análisis de ventas
✔ Dashboards automáticos

📊 Reportes generados

Los archivos se guardan en:

/reports/
    top_clientes.png
    top_productos.png
    ventas_por_dia.png


Ejemplo de análisis realizado:

Top 5 clientes por número de órdenes

Productos más vendidos

Ventas totales por día

📜 Descripción de Scripts
Script	Función
conexion_postgres.py	Conexion centralizada a PostgreSQL
insertar_clientes.py	Poblar tabla de clientes
etl_productos.py	Poblar tabla de productos
generar_ordenes.py	Crear órdenes aleatorias y guardarlas
analisis_ventas.py	Calcular métricas y KPIs
dashboard_ventas.py	Generar gráficos PNG
pipeline_ventas.py	Orquestación en Airflow
📦 Requerimientos

Archivo requirements.txt:

pandas
psycopg2-binary
matplotlib
plotly
kaleido
apache-airflow==2.6.3

🛠️ Mejoras futuras

✔ Agregar notificaciones por correo
✔ Contenerizar scripts en Docker
✔ Crear API para exponer KPIs
✔ Añadir tests unitarios
✔ Integrar CI/CD con GitHub Actions

👨‍💻 Autor

Carlos Gutierrez
Ingeniero de Sistemas | Ciberseguridad | Data Engineering

📧 chgut31@gmail.com

🔗 GitHub: https://github.com/CarlosGutierrezR
