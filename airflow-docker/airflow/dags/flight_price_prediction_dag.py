from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Import our custom classes from the manually created utils folder
from utils.data_ingestion import DataLoader
from utils.data_transformation import DataTransformer
from utils.model_training import RandomForestModel

# The explicit container link to your CSV file inside the mounted volume
DATA_FILE_PATH = '/opt/airflow/data/flights.csv'

# Define the default execution arguments for the workflow runtime
default_args = {
    'owner': 'Admin',
    'depends_on_past': True,
    'start_date': datetime(2023, 9, 19),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Create the master DAG configuration container
dag = DAG(
    'flight_price_prediction_dag',
    default_args=default_args,
    description='An optimized modular DAG for travel price prediction',
    schedule='@daily',  # Set to None for manual execution/testing
    catchup=False,
)

# ------------------------------------------------------------------
# TASK EXECUTION WRAPPERS (Prevents code from running on parse-time)
# ------------------------------------------------------------------

def run_load_data(file_path):
    """Instantiates the loader and pushes loaded dataframe data to XCom."""
    loader = DataLoader(file_path, on_bad_lines='skip')
    return loader.load_data()


def run_transform_data(**kwargs):
    """Pulls raw dataframe from the ingest step via XCom, transforms it, and returns it."""
    ti = kwargs['ti']
    raw_data = ti.xcom_pull(task_ids='load_data_task')
    transformer = DataTransformer()
    return transformer.transform_data(data=raw_data)


def run_model_training(**kwargs):
    """Pulls processed data from the transform step via XCom and trains the ML model."""
    ti = kwargs['ti']
    transformed_data = ti.xcom_pull(task_ids='transform_data_task')
    model_runner = RandomForestModel()
    model_runner.random_forest(data=transformed_data)

# ------------------------------------------------------------------
# AIRFLOW OPERATOR DEFINITIONS
# ------------------------------------------------------------------

# 1. Task to safely isolate and load data inside the environment
load_data_task = PythonOperator(
    task_id='load_data_task',
    python_callable=run_load_data,
    op_args=[DATA_FILE_PATH],  
    dag=dag,
)

# 2. Task to isolate features and apply clean transformation pipelines
transform_data_task = PythonOperator(
    task_id='transform_data_task',
    python_callable=run_transform_data,
    dag=dag,
)

# 3. Task to split configurations and optimize Random Forest execution
random_forest_task = PythonOperator(
    task_id='random_forest_task',
    python_callable=run_model_training,
    dag=dag,  # Removed provide_context=True from here
)

# ------------------------------------------------------------------
# PIPELINE STREAM DEPENDENCIES
# ------------------------------------------------------------------
load_data_task >> transform_data_task >> random_forest_task