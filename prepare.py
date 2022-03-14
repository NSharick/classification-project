#imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#split the telco data function
def split_telco_data(df):
    '''
    This function is for splitting the dataset into train, validate, and test 
    and is used in the preparation function below so that all data prep operations 
    can be done in the notebook with one call
    '''
    train_val, test = train_test_split(df, train_size = 0.8, stratify = df.churn, random_state=123)
    train, validate = train_test_split(train_val, train_size = 0.7, stratify = train_val.churn, random_state=123)
    return train, validate, test

#Prepare Telco dataset for modeling function
def prep_telco(df):
    '''
    This function prepares the dataset to be used for exploration 
    and for building machine learning models. This function keeps the original columns 
    after encoding the categorical variables for ml so that the original columns can be 
    used for data exploration
    '''
    #replace whitespace cells with np.nan so that calculations can be made with the column
    df.total_charges = df.total_charges.replace(' ', np.nan).astype(float)
    #drop foreign key id columns that resulted from the sql query
    df = df.drop(columns = ['payment_type_id', 'internet_service_type_id', 'contract_type_id'])
    #change the valuse in the churn column from "yes/no" to "1/0" for calculating churn rate etc.
    df['churn'] = df['churn'].apply(lambda x: 1 if x == 'Yes' else 0)
    #encode the categorical columns
    encode_cols = [col for col in df.columns if df[col].dtype == 'O']
    encode_cols.remove('customer_id')
    for col in encode_cols:
        dummie_df = pd.get_dummies(df[col], prefix = df[col].name, drop_first = True)
        df = pd.concat([df, dummie_df], axis=1)
    #rename the payment type columns to remove the "()" for functionality in python script
    df = df.rename(columns={'payment_type_Credit card (automatic)':'pay_credit', 'payment_type_Electronic check': 'pay_elec', 'payment_type_Mailed check': 'pay_mail'})
    #split the data using the above splitting function
    train, validate, test = split_telco_data(df)
    #Return the train, validate, and test dataframes
    return train, validate, test






