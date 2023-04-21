from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd
import sys
import os 


modulo_path = os.path.abspath('/opt/airflow/dags/user_defined/to_tables.py')

# Agregamos la ruta a sys.path para que Python la reconozca
sys.path.append(os.path.dirname(modulo_path))


import to_tables as tt

import importlib

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


# File path
file1 = 'dags/data/half_df2.csv'
file2 = 'dags/data/half_df3.csv'

index_pickle_file = 'dags/data/idx.pickle'
lang_pk = 'dags/data/language.pickle'
db_pk = 'dags/data/database.pickle'
fm_pk = 'dags/data/framework.pickle'
plt_pk = 'dags/data/platform.pickle'
dt_pk = 'dags/data/devtype.pickle'


default_args = {
    'owner': 'Noelia',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def load_data(file):
    
    if file==file1:
        force_from_zero = True
    else:
        force_from_zero = False


    if force_from_zero:
        tt.load_init_idplus(index_pickle_file)
        load_init = True

    doesnt_exists = False
    try:
        init_dict = tt.load_generic_dict(index_pickle_file)
    except:
        doesnt_exists = True

    if doesnt_exists:
        load_init=True
    else:
        if init_dict['lang_df'] == 0:
            load_init=True
        else:
            load_init=False

    df, dev_df, job_df, exp_df, lang_df, db_df, framework_df, platform_df, dev_type_df, df_exp_lang, df_exp_db, df_exp_framework, df_exp_platform, \
        df_job_devtype = tt.get_all_tables(file,  index_pickle_file, lang_pk, db_pk, fm_pk, plt_pk, dt_pk, load_init)

    list_df = [dev_df, job_df, exp_df, lang_df, db_df, framework_df, platform_df, dev_type_df, df_exp_lang, df_exp_db, df_exp_framework, df_exp_platform, \
        df_job_devtype]
    return list_df



def postgres_login():
    user = 'postgres'
    password = '25deDiciembre'
    db_name = 'postgres'
    host = 'db.npgjypkiqxhnhhknutbj.supabase.co'
    port = '5432'

    # engine = create_engine(f'postgresql://{user}:{password}@{host}/{db_name}')
    url = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}'
    engine = create_engine(url)

    return engine


def load_to_database(file, load_data, postgres_login):

    engine = postgres_login()
    dev_df, job_df, exp_df, lang_df, db_df, framework_df, platform_df, dev_type_df, df_exp_lang, df_exp_db, df_exp_framework, df_exp_platform, \
        df_job_devtype = load_data(file)
    
        
    lang_df.to_sql('language', con=engine, if_exists='append', index= False)
    db_df.to_sql('database', con=engine, if_exists='append', index= False)

    framework_df.to_sql('framework', con=engine, if_exists='append', index= False)
    platform_df.to_sql('platform', con=engine, if_exists='append', index= False)

    dev_type_df.to_sql('dev_type', con=engine, if_exists='append', index= False)



    exp_df.to_sql('experience', con=engine, if_exists='append', index= False)
    job_df.to_sql('job', con=engine, if_exists='append', index= False)

    df_exp_lang.to_sql('exp_lang', con=engine, if_exists='append', index= False)
    df_exp_db.to_sql('exp_db', con=engine, if_exists='append', index= False)

    df_exp_framework.to_sql('exp_framework', con=engine, if_exists='append', index= False)
    df_exp_platform.to_sql('exp_platform', con=engine, if_exists='append', index= False)

    df_job_devtype.to_sql('job_devtype', con=engine, if_exists='append', index= False)


    dev_df.to_sql('developer', con=engine, if_exists='append', index= False)
    print("Ha terminado de ejecutar la funcion principal")


def load_supabase_task():
    load_to_database(file1, load_data, postgres_login)

def greet():
    import pandas as pd
    # df = pd.read_csv('dags/data/half_df2.csv')
    df = pd.read_csv(file1)
    print("df.shape --> ", df.shape)


with DAG(
    dag_id='dag_incremental_load_v10',
    default_args=default_args,
    start_date=datetime(2023,4,19),
    schedule_interval='0 0 * * *'
) as dag:
    task1 = PythonOperator(
        task_id='load_supabase_task1',
        python_callable=load_supabase_task
        # op_kwargs={'age':20}
    )

    task1