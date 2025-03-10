# Write a program that retrieves the dataset for the "exchequer account (historical series)" 
# from the CSO, and stores it into a file called "cso.json".
# Author: Monika Dabrowska

# import necessary libraries
import requests
import json

# get the data from the CSO API
url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en'

# get the data from the url
response = requests.get(url)
data = response.json()

# print of the status code
print(f'the status code is {response.status_code}')

# write the data to a json file # w = write mode
# https://stackoverflow.com/questions/66576064/api-json-result-to-file 
with open('cso.json', 'w') as file:
    json.dump(data, file)





