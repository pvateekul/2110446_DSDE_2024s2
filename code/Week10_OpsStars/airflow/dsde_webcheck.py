from airflow.utils.dates import days_ago
from airflow import DAG

from airflow.operators.bash import BashOperator

dag = DAG('dsde_webcheck', start_date=days_ago(1))

ping = BashOperator(task_id='http_check', bash_command='curl -s https://www.cp.eng.chula.ac.th > /dev/null', dag=dag)

inform = BashOperator(task_id='inform_status', bash_command='echo "CP website still works!"', dag=dag)

ping >> inform

