from main import main
# Apache airflow
from airflow import DAG
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 2, 6),  # Set the start date of the DAG
}

# Define the DAG
with DAG(
    dag_id = "Weather_DAG",
    default_args=default_args,
    start_date= datetime(2025, 2, 6),
    schedule='*/15 * * * *'
) as dag:
    # Create a task in the DAG
    task = PythonOperator(
    task_id='weather_task',  # Name of the task
    python_callable=main,  # Function to call
    dag=dag,  # The DAG this task belongs to
)
    
task