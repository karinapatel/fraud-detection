#script for pulling new data, predicting, and loading to MongoDB 
import predict_features as pred
import requests

pred_list = []

def add_mongo():
    #website hosting events
    url = 'http://galvanize-case-study-on-fraud.herokuapp.com/data_point'
    #builds a json object
    response = requests.get(url)
    raw_data = response.json()
    #for the case of a single entry or multiple entries and tries to check if they are already added
    if len(raw_data)==43:
        event_id = raw_data['ticket_types'][0]['event_id']
        if event_id not in pred_list:
            pred_list.append(raw_data['ticket_types'][0]['event_id'])
            res = pred.predict(raw_data)
            pred.add_to_mongo(res)
    else:
        for event in raw_data:
            event_id = event['ticket_types'][0]['event_id']
            if event_id not in pred_list:
                pred_list.append(event['ticket_types'][0]['event_id'])
                res = pred.predict(event)
                pred.add_to_mongo(res)
# runs a constant loop checking every minute for a new event from the above url
import timex
starttime=time.time()
while True:
  add_mongo()
  time.sleep(60.0 - ((time.time() - starttime) % 60.0))
