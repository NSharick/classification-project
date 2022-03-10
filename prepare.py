#imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#split the telco data function
def split_telco_data(df):
    train_val, test = train_test_split(df, train_size = 0.8, stratify = df.churn, random_state=123)
    train, validate = train_test_split(train_val, train_size = 0.7, stratify = train_val.churn, random_state=123)
    return train, validate, test

#Prepare Telco dataset for modeling function
def prep_telco(df):
    df.total_charges = df.total_charges.replace(' ', np.nan).astype(float)
    df = df.drop(columns = ['customer_id', 'payment_type_id', 'internet_service_type_id', 'contract_type_id'])
    df['churn'] = df['churn'].apply(lambda x: 1 if x == 'Yes' else 0)
    encode_cols = [col for col in df.columns if df[col].dtype == 'O']
    for col in encode_cols:
        dummie_df = pd.get_dummies(df[col], prefix = df[col].name, drop_first = True)
        df = pd.concat([df, dummie_df], axis=1)
    df = df.rename(columns={'payment_type_Credit card (automatic)':'pay_credit', 'payment_type_Electronic check': 'pay_elec', 'payment_type_Mailed check': 'pay_mail'})
    
    
    train, validate, test = split_telco_data(df)
    
    return train, validate, test






