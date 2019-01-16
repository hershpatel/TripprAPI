import os
import json
from flask import Flask
from flask import jsonify
from flask import make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/seattle")
def getSeattleCluster():
	fp = open('trips/seattle.json', 'r')
	seattle = json.load(fp)
	fp.close()
	return jsonify(seattle)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)