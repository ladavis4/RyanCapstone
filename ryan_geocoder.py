import urllib.request
import json
import csv


class RyanGeocoder():
    def __init__(self):
        pass

    def get_tract(self, long, lat):
        string = 'https://geocoding.geo.census.gov/geocoder/geographies/coordinates?x=' + str(long) + '&y=' + str(lat) + '&vintage=Census2010_Census2010&benchmark=Public_AR_Census2010&format=json&layers=Tract'
        try:
            response = urllib.request.urlopen(string)
        except urllib.error.HTTPError:
            print('Bad request')

        data = json.load(response)

        try:
            tract = int(data['result']['geographies']['Census Blocks'][0]['TRACT'])
        except KeyError:
            print('Bad Key!!')

        return tract

    def load_long_lats(self, path):
        longs = []
        lats = []
        with open(path, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for lines in csv_reader:
                longs.append(lines[10])
                lats.append(lines[11])

        return longs, lats


