from airflow.utils.dates import days_ago
from airflow import DAG

from airflow.operators.bash import BashOperator

dag = DAG('dsde_simplebash', start_date=days_ago(1))

echo = BashOperator(task_id='echo_template', bash_command='echo "run_id = {{ run_id }} and ds = {{ ds }}"', dag=dag)

echo
