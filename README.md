 📌 Proyecto: Data Pipeline de Ventas

Este proyecto implementa un pipeline completo y automatizado para procesar datos de ventas utilizando una arquitectura moderna:

- 🐘 **PostgreSQL** (almacenamiento)
- 🐍 **Python** (ETL, análisis y dashboards)
- 🐳 **Docker & Docker Compose**
- 🌬 **Apache Airflow 2.6.3** (orquestación)
- 📊 **Plotly / Matplotlib** (visualización)

El objetivo es simular un flujo real de datos corporativos, procesarlos y generar reportes diarios, todo automatizado con Airflow.

---

## 🏗 Arquitectura del Pipeline

┌──────────────────────────────┐
│ Datos Iniciales │ ← clientes.csv / productos.csv
└───────────────┬──────────────┘
↓
Generación de Órdenes (Python)
↓
ETL hacia PostgreSQL (Python)
↓
Análisis y KPI de Ventas (Python)
↓
Dashboards Automáticos → PNG (Plotly/Matplotlib)
↓
Orquestación con Airflow (pipeline_ventas)

yaml
Copiar código

---

## 📂 Estructura del Proyecto

data-pipeline-ventas/
│
├── airflow/
│ └── pipeline_ventas.py
│
├── dags/ # Carpeta usada por Airflow
│
├── data/
│ ├── clientes.csv
│ ├── productos.csv
│ └── ordenes.csv
│
├── docker/
│ ├── docker-compose.yml
│ └── docker-compose-airflow.yml
│
├── reports/
│ ├── top_clientes.png
│ ├── top_productos.png
│ └── ventas_por_dia.png
│
├── scripts/
│ ├── conexion_postgres.py
│ ├── insertar_clientes.py
│ ├── etl_productos.py
│ ├── generar_ordenes.py
│ ├── analisis_ventas.py
│ └── dashboard_ventas.py
│
├── requirements.txt
└── README.md

yaml
Copiar código

---

## 🚀 Cómo ejecutar el proyecto

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/CarlosGutierrezR/data-pipeline-ventas.git
cd data-pipeline-ventas
🐘 2️⃣ Levantar PostgreSQL + Adminer
Entrar a la carpeta docker:

bash
Copiar código
cd docker
docker compose up -d
Adminer estará disponible en:

👉 http://localhost:8080

Credenciales

Campo	Valor
Servidor	postgres
Usuario	admin
Contraseña	admin
Base de datos	ventasdb

🌬 3️⃣ Levantar Airflow
Desde la carpeta docker/:

bash
Copiar código
docker compose -f docker-compose-airflow.yml up -d
Airflow estará disponible en:

👉 http://localhost:8081

Credenciales Airflow

Usuario	Contraseña
airflow	airflow

▶️ 4️⃣ Ejecutar el Pipeline
En la interfaz web de Airflow:

Buscar el DAG: pipeline_ventas

Activarlo 🔵

Clic en Trigger DAG

Esto ejecutará automáticamente:

✔ Inserción de clientes
✔ Inserción de productos
✔ Generación de órdenes
✔ ETL hacia PostgreSQL
✔ Análisis de métricas de ventas
✔ Dashboards automáticos en PNG

📊 5️⃣ Reportes generados
Los archivos se guardan en:

bash
Copiar código
/reports/
│── top_clientes.png
│── top_productos.png
└── ventas_por_dia.png
Análisis realizados:
⭐ Top 5 clientes por número de compras

🛒 Productos más vendidos

📅 Ventas totales por día

🧠 Descripción de Scripts
Script	Función
conexion_postgres.py	Conexión centralizada a PostgreSQL
insertar_clientes.py	Poblar tabla de clientes
etl_productos.py	Poblar tabla de productos
generar_ordenes.py	Crear órdenes aleatorias
analisis_ventas.py	Cálculo de KPIs y métricas
dashboard_ventas.py	Generación de gráficos PNG
pipeline_ventas.py	Orquestación completa del pipeline en Airflow

⚙️ Tecnologías Utilizadas
Apache Airflow 2.6.3

PostgreSQL 13

Docker & Docker Compose

Python 3.10

pandas / SQLAlchemy

Plotly / Matplotlib

Redis

📦 Requerimientos (solo si ejecutas Python manualmente)
bash
Copiar código
pip install -r requirements.txt
👨‍💻 Autor
Proyecto desarrollado por Carlos Gutierrez R.
