import os
import json
import datetime
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_restful import Resource, Api, reqparse
from bson.objectid import ObjectId
from bson import json_util


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
    MONGO_URL = "mongodb://localhost:27017/trippr"

app.config['MONGO_URI'] = MONGO_URL
mongo = PyMongo(app)

app.json_encoder = JSONEncoder


"""
CORS
"""
CORS(app)


"""
RESTful
"""
api = Api(app)


"""
Trippr API Endpoints
"""
class Seattle(Resource):
	def get(self):
		fp = open('trips/seattle.json', 'r')
		seattle = json.load(fp)
		fp.close()
		return make_response(jsonify(seattle), 200)

class Trips(Resource):
	def post(self):
		trip = json_util.loads(json_util.dumps(request.json))
		mongo.db.trips.insert_one(trip)
		return make_response(trip['_id'], 200)	

	def get(self):
		_id = request.args.get('_id')
		trip = mongo.db.trips.find_one({'_id' : _id})
		if not trip:
			fp = open('trips/seattle.json', 'r')
			seattle = json.load(fp)
			fp.close()
			seattle['_id'] = _id
			mongo.db.trips.insert_one(seattle)
			return make_response(jsonify(seattle), 200)
		return make_response(jsonify(trip), 200)

api.add_resource(Seattle, '/seattle')
api.add_resource(Trips, '/trips')


# @app.route("/seattle", methods=['GET'])
# def getSeattleCluster():
# 	fp = open('trips/seattle.json', 'r')
# 	seattle = json.load(fp)
# 	fp.close()
# 	return make_response(jsonify(seattle), 200)

# # save trip
# @app.route("/trips/save", methods=['POST'])
# def saveTrip():
# 	trip = json_util.loads(request.get_json())
# 	mongo.db.trips.insert_one(trip)
# 	return make_response(trip['_id'], 200)

# # add place
# @app.route("/places/add/<tripID>", methods=['POST'])
# def addPlace(tripID):
# 	data = request.get_json()
# 	return make_response(tripID, 200)

# # delete place
# @app.route("/places/remove/<tripID>", methods=['POST'])
# def removePlace(tripID):
# 	data = request.get_json()
# 	return make_response(tripID, 200)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
