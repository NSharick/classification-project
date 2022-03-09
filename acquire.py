#Get the Telco data from the database and join all four tables into the one dataframe
def get_telco_data():
    filename = 'telco.csv'
    
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)
    
    query = '''
    SELECT * FROM customers
    JOIN contract_types USING (contract_type_id)
    JOIN internet_service_types USING (internet_service_type_id)
    JOIN payment_types USING (payment_type_id)
    '''
    
    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, get_db_url('telco_churn'))
    df.to_csv(filename, index=False)
    return df  

    