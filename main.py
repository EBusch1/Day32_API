# Day 32 API

# Response guide
# 1XX: Hold on
# 2XX: Here you go (success)
# 3XX: Go away (redirection)
# 4XX: You(client) screwed up
# 5XX: I(server) screwed up

import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
print(response)
print(response.status_code)
# response = requests.get(url='http://api.open-notify.org/is-now.json')
# print(response)
# print(response.status_code)
#
# # Use this for exceptions!
# response.raise_for_status()

# Our JSON data
response_data = response.json()
print(response_data)

# JSON data works like dictionaries!
response_data = response.json()['iss_position']
print(response_data)

# With layers!
response_data = response.json()['iss_position']['latitude']
print(response_data)

# And can be used!
iss_coord = (response.json()['iss_position']['latitude'],response.json()['iss_position']['longitude'])
print(iss_coord)

