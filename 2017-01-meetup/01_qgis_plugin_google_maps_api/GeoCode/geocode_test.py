import json, requests

googleApiUrl = 'https://maps.googleapis.com/maps/api/geocode/'
googleApiKey = 'AIzaSyBypRKpFU3eF85J311C8Y8GhsXEuSxja7E'
format = 'json'

def getGeoCode(address):
    request = googleApiUrl + format + '?key=' + googleApiKey + '&address=' + address
    print request
    try:
        return requests.get(request)
    except requests.ConnectionError as error:
        return False




#MAIN

address = 'Slovenska 12, Ljubljana'
response = getGeoCode(address.replace(" ", "+"))
if response:
    content = json.loads(response.content)
    for result in content['results']:
        print result['address_components']
        for component in result['address_components']:
            print component['types'][0] == 'street_number'