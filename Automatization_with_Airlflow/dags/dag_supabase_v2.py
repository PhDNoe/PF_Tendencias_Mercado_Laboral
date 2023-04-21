# *****************************************************************************
# ****************************     Import zone    *****************************
# *****************************************************************************
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd
import sys
import os 
from datetime import datetime, timedelta
import time

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.contrib.sensors.file_sensor import FileSensor
import requests

modulo_path = os.path.abspath('/opt/airflow/dags/user_defined/to_tables.py')
# Add path to sys.path 
sys.path.append(os.path.dirname(modulo_path))
import to_tables as tt
from db_credential_info import get_supabase_credentials

# *****************************************************************************
# ***************************  Path definition zone  **************************
# *****************************************************************************


index_pickle_file = 'dags/data/idx.pickle'
lang_pk = 'dags/data/language.pickle'
db_pk = 'dags/data/database.pickle'
fm_pk = 'dags/data/framework.pickle'
plt_pk = 'dags/data/platform.pickle'
dt_pk = 'dags/data/devtype.pickle'

# Sensors info
directory = "dags/data/incremental_csv/"
filename = "non_first_file.csv"

directory_init = "dags/data/init_csv/"
filename_init = "first_file.csv"

# *****************************************************************************
# *****************  Default args definitionfor dag zone   ********************
# *****************************************************************************

default_args = {
    'owner': 'Noelia',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}



# *****************************************************************************
# *************** Utils function definition zone  *****************************
# *****************************************************************************
def load_init_data(file):
    """
        This function Check wheather or not the file is the first file being 
        uploaded to db.
        If not, it should be load the dictionaries with unique dictionaries

        It has only one input parameter, being the name of the file

        It has many output parameters, one for each table being uploaded
    """
    force_from_zero = True

    if force_from_zero:
        tt.load_init_idplus(index_pickle_file)
        load_init = True

    # doesnt_exists = False
    # try:
    #     init_dict = tt.load_generic_dict(index_pickle_file)
    # except:
    #     doesnt_exists = True

    # if doesnt_exists:
    #     load_init=True
    # else:
    #     if init_dict['lang_df'] == 0:
    #         load_init=True
    #     else:
    #         load_init=False

    df, dev_df, job_df, exp_df, lang_df, db_df, framework_df, platform_df, dev_type_df, df_exp_lang, df_exp_db, df_exp_framework, df_exp_platform, \
        df_job_devtype = tt.get_all_tables(file,  index_pickle_file, lang_pk, db_pk, fm_pk, plt_pk, dt_pk, load_init)

    list_df = [dev_df, job_df, exp_df, lang_df, db_df, framework_df, platform_df, dev_type_df, df_exp_lang, df_exp_db, df_exp_framework, df_exp_platform, \
        df_job_devtype]
    return list_df

def load_incremental_data(file):
    """
        This function Check wheather or not the file is the first file being 
        uploaded to db.
        If not, it should be load the dictionaries with unique dictionaries

        It has only one input parameter, being the name of the file

        It has many output parameters, one for each table being uploaded
    """
    
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
    """
        This info is private, 
    """
    supabase_credentials = get_supabase_credentials()
    user = supabase_credentials['user']
    password = supabase_credentials['password']
    db_name = supabase_credentials['db_name']
    host = supabase_credentials['host']
    port = supabase_credentials['port']

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

# task 3
def load_init_supabase_task():
    load_to_database(directory_init  + filename_init, load_init_data, postgres_login)


# task 4
def load_incremental_supabase_task():
    load_to_database(directory  + filename, load_incremental_data, postgres_login)



with DAG(
    dag_id='dag_incremental_load_v30',
    default_args=default_args,
    start_date=datetime(2023,4,21),
    schedule_interval='@daily',
    catchup=False,
    max_active_runs=1
) as dag:
    # task1
    file_sensor_init = FileSensor(
        task_id="file_sensor_init_task",
        filepath=directory_init + filename_init,
        poke_interval=5,
        timeout=300,
        fs_conn_id="fs_default",
    )

    # task2
    file_sensor_incremental = FileSensor(
        task_id="file_sensor_incremental_task",
        filepath=directory  + filename,
        poke_interval=5,
        timeout=300,
        fs_conn_id="fs_default",
    )
    
    # task 3
    task3 = PythonOperator(
        task_id='load_supabase_init_task',
        python_callable=load_init_supabase_task
        
    )

    task4 = PythonOperator(
        task_id='load_supabase_incremental_task',
        python_callable=load_incremental_supabase_task
        
    )


    # establecer dependencias de los sensores en las tareas
    task3.set_upstream(file_sensor_init)
    task4.set_upstream(file_sensor_incremental)