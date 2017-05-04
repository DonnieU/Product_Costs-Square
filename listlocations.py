# Purpose: List Locations from Square

#!/usr/bin/python
import httplib, urllib, json

# All requests to the Square Connect API require an access token in an
# Authorization header. Specify your application's personal access token here
# (available from https://connect.squareup.com/apps)
access_token = 'REPLACE_ME'

#access_token = 'sandbox-sq0atb-j77JKUZl_MB3TftQbCwbdQ'

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

# Pretty-print the locations array.
print json.dumps(locations, indent=2, separators=(',',': '))
