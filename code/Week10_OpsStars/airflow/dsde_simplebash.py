from airflow.utils.dates import days_ago
from airflow import DAG

from airflow.operators.bash import BashOperator
import pendulum
import datetime

dag = DAG('dsde_simplebash',  start_date=pendulum.today(
    'UTC').add(days=-1), schedule=datetime.timedelta(days=1))

echo = BashOperator(task_id='echo_template',
                    bash_command='echo "run_id = {{ run_id }} and ds = {{ ds }}"', dag=dag)

echo
