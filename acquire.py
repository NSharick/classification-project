#Imports for the function:
import numpy as np
import pandas as pd
from env import get_db_url
import os

#Get the Telco data from the database and join all four tables into the one dataframe
def get_telco_data():
    '''
    this function will check if there is already a copy of the dataset
    in the current working directory, read from that file if there is, 
    and pull a new copy from the database if there is not, it will also 
    save a copy to the local directory if it pulls a new one
    '''
    #assign the file name
    filename = 'telco.csv'
    #check if the file exists in the current directory and read it if it is
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)
    #assign the sql query to a variable for use
    query = '''
    SELECT * FROM customers
    JOIN contract_types USING (contract_type_id)
    JOIN internet_service_types USING (internet_service_type_id)
    JOIN payment_types USING (payment_type_id)
    '''
    #if needed pull a fresh copy of the dataset from the database and save localy
    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, get_db_url('telco_churn'))
    df.to_csv(filename, index=False)
    return df  

    