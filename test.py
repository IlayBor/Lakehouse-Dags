from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define the basic parameters for the DAG
with DAG(
    dag_id="test_hello_world",
    start_date=datetime(2024, 1, 1),  # A date in the past is required
    schedule=None,  # None means it will only run manually
    catchup=False,  # Prevents Airflow from running past dates
    tags=["test"],
) as dag:
    # Define a single task that echoes "Hello, World!"
    hello_task = BashOperator(
        task_id="print_hello",
        bash_command="echo 'Hello, World!'",
    )
