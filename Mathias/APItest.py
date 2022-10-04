import requests
import pandas as pd
import matplotlib.pyplot as plt

file = "testdata.txt"

plasser = {"Heim": "SN65230", "Melhus": "SN68270", "Åfjord": "SN71810"}

# URL = "frost.met.no/api.html/"

client_id = "ca187224-be36-4dd7-96a7-67908ae7af90"

# Define endpoint and parameters
endpoint = 'https://frost.met.no/observations/v0.jsonld'
parameters = {
    'sources': f'{plasser["Heim"]}, {plasser["Melhus"]}, {plasser["Åfjord"]}',
    'elements': 'mean(air_temperature P1D),sum(precipitation_amount P1D),mean(wind_speed P1D)',
    'referencetime': '2021-01-01/2022-09-01',
}
# Issue an HTTP GET request
r = requests.get(endpoint, parameters, auth=(client_id,''))
# Extract JSON data
json = r.json()

# Check if the request worked, print out any errors
if r.status_code == 200:
    data = json['data']
    print('Data retrieved from frost.met.no!')
else:
    print('Error! Returned status code %s' % r.status_code)
    print('Message: %s' % json['error']['message'])
    print('Reason: %s' % json['error']['reason'])


with open(file, "w+") as fil:
    for i in data:
        # fil.write(str(i))
        id = i["sourceId"]
        tid = ((i["referenceTime"]).split("T"))[0]
        nedbør = str(i["observations"][0]["value"])
        fil.write(f"{id};{tid};{nedbør}\n")



