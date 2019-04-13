import numpy as np
import pandas as pd
from Clean import clean
from tickets_sold import get_num_tickets_sold
from transform import transform_train
import pickle
from sklearn.ensemble import RandomForestClassifier



df = pd.read_json("data/data.json")

def final_model(df):
    
    #final model we decided on through selection
    model = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=None, max_features='log2', max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, n_estimators=400, n_jobs=1,
            oob_score=False, random_state=None, verbose=0,
            warm_start=False)
    
    #get the data in the form we want according to transform function
    X,y = transform_train(df)
    
    #fit the model
    model.fit(X,y)
    
    with open('website/model.pkl', 'wb') as f:
        # Write the model to a file.
        pickle.dump(model, f)
    