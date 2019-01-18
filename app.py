import os
import json
import datetime
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

"""
MongoDB
"""
MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017/rest"

app.config['MONGO_URI'] = MONGO_URL
mongo = PyMongo(app)

app.json_encoder = JSONEncoder


"""
CORS
"""
CORS(app)


"""
Trippr API Endpoints
"""
@app.route("/seattle", methods=['GET'])
def getSeattleCluster():
	fp = open('trips/seattle.json', 'r')
	seattle = json.load(fp)
	fp.close()
	return jsonify(seattle)

# save trip
@app.route("/saveTrip/<tripID>", methods=['POST'])
def saveTrip(tripID):
	data = request.get_json()
	return tripID

# add place
@app.route("/addPlace/<tripID>", methods=['POST'])
def addPlace(tripID):
	data = request.get_json()
	return tripID

# delete place
@app.route("/removePlace/<tripID>", methods=['POST'])
def removePlace(tripID):
	data = request.get_json()
	return tripID

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


"""

NOTES

Processing Incoming Request Data 
- https://scotch.io/bar-talk/processing-incoming-request-data-in-flask

MongoDB / Flask / Heroku 
- https://spapas.github.io/2014/06/30/rest-flask-mongodb-heroku/
- https://medium.com/@riken.mehta/full-stack-tutorial-flask-react-docker-ee316a46e876


"""