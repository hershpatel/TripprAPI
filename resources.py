import json
from flask import request, abort
from flask.ext import restful
from flask.ext.restful import reqparse
from flask_rest_service import app, api, mongo
from bson.objectid import ObjectId

class Trip(restful.Resource):
	 def __init__(self, *args, **kwargs):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('tripID', type=str)
        super(Trip, self).__init__()

     def get(self):
     	# grab trip 
        return  None

     def post(self):
     	# save trip
     	return None

class Root(restful.Resource):
    def get(self):
        return {
            'status': 'OK',
            'mongo': str(mongo.db),
        }

api.add_resource(Root, '/')
api.add_resource(Trip, '/Trip/<ObjectId:tripID>')