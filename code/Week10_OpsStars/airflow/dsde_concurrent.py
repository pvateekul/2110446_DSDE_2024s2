from airflow.utils.dates import days_ago
from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

import pendulum
import datetime

# 'with' enables DAG to become context managers; automatically assign new operators to that DAG
with DAG('dsde_concurrent', start_date=pendulum.today('UTC').add(days=-1), schedule=datetime.timedelta(days=1)) as dag:
    start = EmptyOperator(task_id='start_task')
    ping = BashOperator(task_id='cp_check',
                        bash_command='curl https://www.cp.eng.chula.ac.th')
    ping2 = BashOperator(task_id='eng_check',
                         bash_command='curl https://www.eng.chula.ac.th')
    inform = BashOperator(task_id='inform_status',
                          bash_command='echo "CP website still works!"')

    # creating DAG dependencies can be a long flow or multiple short flows
    # start >> [ping, ping2] >> inform
    start >> [ping, ping2]
    ping >> inform
    ping2 >> inform
