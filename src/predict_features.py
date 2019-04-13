import pickle
import pandas as pd
from pymongo import MongoClient
from transform import transform_test
from treeinterpreter import treeinterpreter as ti


#takes in one single json line from the live data
def predict(row):
    df = pd.DataFrame.from_dict([row], orient='columns')
    #open model RF
    with open('website/model.pkl', 'rb') as f:
        model = pickle.load(f)

    df1 = transform_test(df)

    #predict probability using model
    prediction = model.predict_proba(df1.values.reshape(1, -1))[0][1]

    row['prediction'] = prediction

    #determine contribution of features to prediction using treeinterpreter
    prediction, bias, contributions = ti.predict(model, df1.values.reshape(1, -1))
    #empty list to hold important features which contributed to prediction
    important_features = []
    #names for features
    column_features = ['name_length','num_payouts','user_age','org_facebook','org_twitter','body_length','gts','sale_duration','tickets_sold']
    #take the top 3 features which had the highest contribution
    for feature, key in sorted(zip(abs(contributions[0][:,1]),column_features))[::-1][:3]:
        important_features.append(key)
        
    
    row['contributions'] = important_features

    #returns the prob of fraud which we can later classify using the threshold chosen
    return row

def add_to_mongo(row):
    #start up Mongo
    client = MongoClient()
    db = client['fraud']
    coll=db['predicted']
    coll.insert(row)
        