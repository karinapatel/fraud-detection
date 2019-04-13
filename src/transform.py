import numpy as np
import pandas as pd
from Clean import clean
from tickets_sold import get_num_tickets_sold

#df = pd.read_json("data/data.json")

#train data transform:
def transform_train(df_train):
    
    #add targets to train df according to fraudster fxn in clean
    df = clean(df_train)
    
    #extract tickets sold feature from ticket type
    df['tickets_sold'] = get_num_tickets_sold(df)
    
    #grab the subset of columns we want to use for classification
    subset = df[['name_length','num_payouts','user_age','org_facebook','org_twitter','body_length','gts','sale_duration','tickets_sold','Target']]
    
    #split into X and y according to target and features
    X = subset[['name_length','num_payouts','user_age','org_facebook','org_twitter','body_length','gts','sale_duration','tickets_sold']]
    y = subset['Target']
    
    #fill nulls with -1 befor splitting into train and split
    df['org_facebook'] = df['org_facebook'].fillna(-1)
    df['org_twitter'] = df['org_twitter'].fillna(-1)
    df['sale_duration'] = df['sale_duration'].fillna(-1)
    
    #returns the dataframe for X and y used in our model selection
    return X,y
    
def transform_test(df_test):
    
    #no adding targets because we have none..that is what we are predicting!
    
    #extract tickets sold feature from ticket type
    df_test['tickets_sold'] = get_num_tickets_sold(df_test)
    
    #grab the subset of columns we want to use for classification
    df = df_test[['name_length','num_payouts','user_age','org_facebook','org_twitter','body_length','gts','sale_duration','tickets_sold']]
    
    #fill nulls with -1 befor splitting into train and split
    df['org_facebook'] = df['org_facebook'].fillna(-1)
    df['org_twitter'] = df['org_twitter'].fillna(-1)
    df['sale_duration'] = df['sale_duration'].fillna(-1)

    return df