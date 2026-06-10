FROM apache/airflow:2.7.2

USER root
RUN apt-get update && \
    apt-get -y install git && \
    apt-get clean 
    
    
USER airflow

RUN pip install --no-cache-dir scikit-learn pandas numpy joblib