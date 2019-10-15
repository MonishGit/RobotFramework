import json
import  requests
import  jsonpath


api_url="https://jnj-test.apigee.net/hw-endeavour-app/v1/countries"
# odisc = '{"K1":"Test1","K2":"Test2","K3":1223}'

#This will conver dictionary to json file
# json_parsing = json.loads(odisc)
# print (str(json_parsing['K2']))

# Stpe 1- Performing GET request using python and parsing the data. must needed inbuild libray - json, requests and package jasonpath

get_response_fromURL= requests.get(api_url)

#Stpe 2- validate response code e.g. 200, 201 etc. it always start with assert

assert get_response_fromURL.status_code == 200

#Stpe 3- parser the response in json format

json_parsData = json.loads(get_response_fromURL.text)

# print (json_parsData)

# Step 4- Fetch the required data from the json data extracted e.g. finding list of the country from the json data

# extract_one_country = jsonpath.jsonpath(json_parsData,'$..[0].name')

# print(extract_one_country[0])

# extract_all_countries

for val in json_parsData:
    print (val['countryCode'])

