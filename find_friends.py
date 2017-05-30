import math, json

def read_json(file):
	try:
	    with open(file, 'r') as data_file:
	        data = json.load(data_file)
		return data
	except ValueError:
		return "Invalid JSON"	

def find_distance(latitude1, longitude1, latitude2, longitude2):

	try:		
		if not (latitude1 or latitude2 or longitude1 or longitude2):
			return

		diff_longitude = (float(longitude2) - float(longitude1))
		diff_longitude = math.radians(diff_longitude)

		# convert degree into radians
		latitude1 = math.radians(float(latitude1))
		latitude2 = math.radians(float(latitude2))

		earth_radius = 6371

		distance = math.acos(math.sin(latitude1)*math.sin(latitude2) + math.cos(latitude1)*math.cos(latitude2)*math.cos(diff_longitude)) * earth_radius
		
		return distance     # distance in km
	
	except Exception as e:
		return e
		

def find_friends(friends_list):
	try:		
		friends_within_radius = []
		
		if not friends_list:
			return
		
		for friend in friends_list:
			if not (('latitude' in friend) or ('longitude' in friend)):
				continue

			lat = friend['latitude']
			longt = friend['longitude']	
			
			distance = find_distance(12.935076, 77.614277, lat, longt)

			if distance <= 100 and distance >= 0:

				if ('name' in friend) and ('user_id' in friend):
					name = friend['name'].encode('ascii','ignore')
					user_id = friend['user_id']
					friends_within_radius.append([name, user_id])

		return sorted(friends_within_radius, key=lambda x: x[1])
	except Exception as e:
		return e	


if __name__ == "__main__":
	friends_list = read_json('customers.json')
	print find_friends(friends_list)
	