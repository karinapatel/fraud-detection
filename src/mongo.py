#load training data into Mongo as first step
from pymongo import MongoClient
import json

#opens the live data file
#will replace path later, for now just using train data
with open('data/data.json') as json_file:  
    data = json.load(json_file)

#start up Mongo
client = MongoClient()
db = client['fraud']
coll=db['train_data']

#insert the data into the collection train_data
for row in data:
    coll.insert(row)