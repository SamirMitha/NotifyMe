# Samir Mitha - (c) 2021
import googlemaps
import requests, json

def fetch_distance(origins, destinations, gmaps_API_key):
	"""Gets the distance and travel time between and origin and destination

    Parameters
    ----------
    origins : str
    	Address
    destination: str
    	Address
    gmaps_API_key: str
    	The GoogleMaps API key to call on googlemaps functions

    Returns
    -------
    distance: int
        The travel distance in meters
    travel_time: int
    	The travel time in seconds
    """
	gmaps = googlemaps.Client(key=gmaps_API_key)
	# required parameters
	origins = origins.replace(' ', '+')
	destinations = destinations.replace(' ', '+')
	# optional parameters
	mode = mode.replace(' ', '+')
	avoid = avoid.replace(' ', '+')
	units = units.replace(' ', '+')
	arrival_time = arrival_time.replace(' ', '+')
	departure_time = departure_time.replace(' ', '+')
	traffic_model = traffic_model.replace(' ', '+')
	transit_mode = transit_mode.replace(' ', '+')
	transit_routing_preference = transit_routing_preference.replace(' ', '+')
	# creating request
	url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
	# units
	if units == 'imperial':
		url_units = 'units=' + units
	else:
		url_units = 'units=metric'
	# origins
	url_origins = '&origins=' + origins
	# destinations
	url_destinations = '&destinations=' + destinations
	# mode
	if mode != '':
		url_mode = '&mode=' + mode
	else:
		url_mode = ''
	# avoid
	if avoid != '':
		url_avoid = '&avoid=' + avoid
	else:
		url_avoid = ''
	# arrival_time
	if arrival_time != '':
		url_arrival_time = '&arrival_time=' + arrival_time
	else:
		url_arrival_time = ''
	# departure_time
	if departure_time != '':
		url_departure_time = '&departure_time=' + departure_time
	else:
		url_departure_time = ''
	# traffic_model
	if traffic_model != '':
		url_traffic_model = '&traffic_model=' + traffic_model
	else:
		url_traffic_model = ''
	# transit_mode
	if transit_mode != '':
		url_transit_mode = '&transit_mode=' + transit_mode
	else:
		url_transit_mode = ''
	# transit_routing_preference
	if transit_routing_preference != '':
		url_transit_routing_preference = '&transit_routing_preference=' + transit_routing_preference
	else:
		url_transit_routing_preference = ''
	# creating url
	r = requests.get(url + url_units + url_origins + url_destinations + url_mode + url_avoid + url_arrival_time + url_departure_time + url_traffic_model + url_transit_mode + url_transit_routing_preference + '&key=' + gmaps_API_key)
	x = r.json()
	distance = int(x['rows'][0]['elements'][0]['distance']['value'])
	travel_time = int(x['rows'][0]['elements'][0]['duration']['value'])
	return distance, travel_time

def fetch_directions(origins, destinations, gmaps_API_key):
	"""Gets the line number and agency of public transit required

    Parameters
    ----------
    origins : str
    	Address
    destination: str
    	Address
    gmaps_API_key: str
    	The GoogleMaps API key to call on googlemaps functions

    Returns
    -------
    short_line: list
        A list of public transit agency line numbers
    agency: list
    	A list of public transit agency names
    """
	gmaps = googlemaps.Client(key=gmaps_API_key)
	# required parameters
	origins = origins.replace(' ', '+')
	destinations = destinations.replace(' ', '+')
	url = 'https://maps.googleapis.com/maps/api/directions/json?'
	r = requests.get(url + url_origins + url_destinations + '&key=' + gmaps_API_key)
	r = requests.get(url)
	x = r.json()
	num = len(x['routes'][0]['legs'][0]['steps'])
	for i in range(num):
		if x['routes'][0]['legs'][0]['steps'][i]['travel_mode'] == 'TRANSIT':
			short_line[i] = x['routes'][0]['legs'][0]['steps'][i]['transit_details']['line']['short_name']
			agency[i] = x['routes'][0]['legs'][0]['steps'][i]['transit_details']['line']['agencies'][0]['name']
	return(short_line, agency)