from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

PY = "docker exec python-container python"
SUBMIT = "docker exec python-container /opt/spark/bin/spark-submit"

with DAG(
    dag_id="price_intelligence_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["prices"],
) as dag:
    scrape = BashOperator(task_id="scrape_stores", bash_command=f"{PY} /app/scrapers/run_all.py")
    bronze = BashOperator(task_id="bronze", bash_command=f"{SUBMIT} /app/jobs/bronze.py")
    silver = BashOperator(task_id="silver", bash_command=f"{SUBMIT} /app/jobs/silver.py")
    gold = BashOperator(task_id="gold", bash_command=f"{SUBMIT} /app/jobs/gold.py")
    serving = BashOperator(task_id="load_serving", bash_command=f"{SUBMIT} /app/jobs/to_postgres.py")

    scrape >> bronze >> silver >> gold >> serving
