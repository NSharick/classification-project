#Prepare Telco dataset function
def prep_telco(df):
    df.total_charges = df.total_charges.replace(' ', np.nan).astype(float)
    columns_drop = ['customer_id', 'payment_type_id', 'internet_service_type_id', 'contract_type_id']
    df = df.drop(columns = columns_drop)
    encode_cols = [col for col in df.columns if df[col].dtype == 'O']
    for col in encode_cols:
        dumb_df = pd.get_dummies(df[col], prefix = df[col].name, drop_first = True)
        df = pd.concat([df, dumb_df], axis=1)
        df = df.drop(columns=[col])
    return df


#split the telco data function

