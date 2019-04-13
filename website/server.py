from flask import Flask, render_template, request, jsonify, Response
import pickle
import pandas as pd
from pymongo import MongoClient
import pymongo

#create the app object that will route our calls
app = Flask(__name__)
# open mongo to get our data out of it
client = MongoClient('13.56.168.145')
db = client['fraud']
coll = db['predicted2']


@app.route('/',methods = ['GET'])
#Create home page that is formatted by home.html file
def home():
    return render_template('home.html')

model = pickle.load(open('model.pkl','rb'))

@app.route('/score',methods=['GET'])
# Create score webpage
def dashboard():
    # Cursor item that goes through mongo and gets observations
    m=list(coll.find().sort('_id', pymongo.DESCENDING).limit(100))
    # Create empty dictionary to add events with selected features
    events = dict()
    # Creates id_list and count to check to make sure there are no duplicates
    id_list = []
    count = 0
    for i,event in enumerate(list(m)):
        # Breaks when we get 50 observations from mongo
        if count==50:
            break
        if event['ticket_types'][0]['event_id'] not in id_list:
            # Create new feature that tells us the level of predicted fraud
            if event['prediction'] <= 0.5:
                level = 'low'
            elif event['prediction'] <= 0.75:
                level = 'medium'
            else:
                level = 'high'
            event['level'] = level
            # Adding observations to our dictionary with id, name, prediction probability, prediction level, and features that contributed
            events[count] = [event['ticket_types'][0]['event_id'],event['name'],event['prediction'],event['level'],event['contributions']]
            count +=1
            id_list.append(event['ticket_types'][0]['event_id'])
  
    return render_template('score.html',result=events)

@app.route('/fake_news',methods = ['GET'])
# Creates page that says fake news
def fake_news():
    return render_template('fake_news.html')

@app.route('/metrics',methods= ['GET'])
# Creates page for graphs and visuals
def metrics():
    return render_template('metrics.html')

#port to run locally
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3335,debug=True)