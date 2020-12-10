import urllib.request
import json

class RyanGeocoder():
    def __init__(self):
        pass

    def get_tract(self, long, lat): # Function pulls tract number from census website given lat/lon.
        # Create the custom url
        string = 'https://geocoding.geo.census.gov/geocoder/geographies/coordinates?x=' + str(long) + '&y=' + str(lat) + '&vintage=Census2010_Census2010&benchmark=Public_AR_Census2010&format=json&layers=Tract'
        try: # try to request the tract
            response = urllib.request.urlopen(string)
            data = json.load(response)
            tract = int(data['result']['geographies']['Census Blocks'][0]['TRACT'])
        except: # if an error occurs, set the tract number to 0.
            tract = 0;

        return tract