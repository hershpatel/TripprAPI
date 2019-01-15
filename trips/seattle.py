import json
import requests

seattle = 'seattle.csv'

query = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=seattle+"
api_key = "&language=en&key=AIzaSyCrrxZxajW7IfAoiZTWHymyfKXsnZhZ2Ek"

def storeSeattleGroups():
	fp = open('seattle.csv', 'r')
	lines = fp.readlines()
	fp.close()
	lines = [line.split(',') for line in lines[1:]]
	lines = [(line[0], line[1].split("\t")[0][1:]) for line in lines]

	seattle = {'num_groups':5, 'groups':[]}
	colors = {'A':'#6666ff', 'B':'#66cdff', 'C':'#ee9713', 'D':'#5ddb52', 'E':'#e15656'}
	groups = set()
	for line in lines:
		group = line[0]
		thing = line[1]
		if not group in groups:
			seattle['groups'].append({})
			seattle['groups'][-1]['group_name'] = group
			seattle['groups'][-1]['color'] = colors[group]
			seattle['groups'][-1]['places'] = []
			groups.add(group)
		info = json.loads(requests.get(query+thing+api_key).text)['results']
		address = info[0]['formatted_address']
		lat = info[0]['geometry']['location']['lat']
		lon = info[0]['geometry']['location']['lng']
		rating = info[0]['rating']
		thing = {'name':thing, 'address':address, 'coord':[lon,lat], 'lon':lon, 'lat':lat, 'rating':rating}
		seattle['groups'][-1]['places'].append(thing)

	fp = open('seattle.json', 'w')
	json.dump(seattle, fp, indent=4, separators=(',', ': '), sort_keys=True)
	fp.close()

if __name__ == '__main__':
	storeSeattleGroups()