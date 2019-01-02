import json
import requests

seattle = 'seattle.csv'

query = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=seattle+"
api_key = "&language=en&key=AIzaSyCrrxZxajW7IfAoiZTWHymyfKXsnZhZ2Ek"

def storeSeattleClusters():
	fp = open('seattle.csv', 'r')
	lines = fp.readlines()
	fp.close()
	lines = [line.split(',') for line in lines[1:]]
	lines = [(line[0], line[1].split("\t")[0][1:]) for line in lines]

	seattle = {'num_clusters':5, 'clusters':{}}
	for line in lines:
		cluster = line[0]
		thing = line[1]
		if not cluster in seattle['clusters']:
			seattle['clusters'][cluster]=[]
		info = json.loads(requests.get(query+thing+api_key).text)['results']
		address = info[0]['formatted_address']
		lat = info[0]['geometry']['location']['lat']
		lon = info[0]['geometry']['location']['lng']
		rating = info[0]['rating']
		thing = {'name':thing, 'address':address, 'lat':lat, 'lon':lon, 'rating':rating}
		seattle['clusters'][cluster].append(thing)

	fp = open('seattle.json', 'w')
	json.dump(seattle, fp, indent=4, separators=(',', ': '), sort_keys=True)
	fp.close()

if __name__ == '__main__':
	storeSeattleClusters()