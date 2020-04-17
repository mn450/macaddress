# importing the requests library
import requests
import sys

search = sys.argv[1]
# api-endpoint
URL = "https://api.macaddress.io/v1"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'apiKey': 'at_2IwFcMoQvqQsJBa1l5shU0BzGavGH', 'output':'json', 'search': search}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
data = r.json()
# print(data)

companyName = data['vendorDetails']['companyName']
print("Company Name ==",companyName)
