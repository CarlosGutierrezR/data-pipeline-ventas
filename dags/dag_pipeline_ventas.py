from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "carlos",
    "retries": 1,
    "retry_delay": timedelta(minutes=2)
}

with DAG(
    dag_id="pipeline_ventas",
    default_args=default_args,
    description="Pipeline ETL de ventas",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False
):

    extraer_datos = BashOperator(
        task_id="extraer_datos",
        bash_command="python /opt/airflow/scripts/analisis_ventas.py"
    )

    generar_reportes = BashOperator(
        task_id="generar_reportes",
        bash_command="python /opt/airflow/scripts/dashboard_ventas.py"
    )

    extraer_datos >> generar_reportes
