import os
import json
from flask import Flask
from flask import jsonify
from flask import make_response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# load default trip
@app.route("/seattle")
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

Flask POST Data Info

https://scotch.io/bar-talk/processing-incoming-request-data-in-flask

parameter data - tripprapi.com/example?key=value&key2=value2
	value = request.args.get('key') --> if this doesn't exist, it will return None (optional)
	value2 = request.args['key2'] --> if this doesn't exist, will cause an error (required)

form / json data - watch video

"""