# Purpose: List Items from Square

#!/usr/bin/python
import httplib, urllib, json

# All requests to the Square Connect API require an access token in an
# Authorization header. Specify your application's personal access token here
# (available from https://connect.squareup.com/apps)
f = open('access_token_p','r')
access_token = f.readline().strip() # .strip() removes \n from string
f.close()

# In addition to an Authorization header, requests to the Connect API should
# include the indicated Accept and Content-Type headers.
request_headers = {'Authorization': 'Bearer ' + access_token,
								'Accept':				'application/json',
								'Content-Type':	'application/json'}

# Send a GET request to the ListLocations endpoint and obtain the response.
connection = httplib.HTTPSConnection('connect.squareup.com')
request_path = '/v2/locations'
connection.request('GET', request_path, '', request_headers)
response = connection.getresponse()

# Convert the returned JSON body into an array of locations you can work with.
locations = json.loads(response.read())

# Parse location id
# Dict --> List --> Dict
l_id = locations['locations'][0].get('id')

# Pretty-print the locations array.
#print json.dumps(locations, indent=2, separators=(',',': '))

# Send a GET request to List Items
request_path = '/v1/' + l_id + '/items'
connection.request('GET', request_path, '', request_headers)
response = connection.getresponse()

items = json.loads(response.read())
print json.dumps(items, indent=2, separators=(',',': '))
