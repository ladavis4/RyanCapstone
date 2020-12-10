import ryan_geocoder
import csv

coder = ryan_geocoder.RyanGeocoder()

oldfile = open('Alcohol Data Input.csv', 'r'); # File that stores the lat/lon
csvreader = csv.reader(oldfile, delimiter=',');
newfile = open('Alcohol Data Output.csv', 'w', newline=''); # File where we want to save the tract in a new column
csvwriter = csv.writer(newfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

for line in csvreader:
    long=line[10] # longtitude is stored in column 10, where the leftmost column is column 0.
    lat=line[11] # latitude is stored in column 11, where the leftmost column is column 0.
    tract = coder.get_tract(long, lat) # push lat/long to site and pull tract
    #newfile.flush() # refresh the file. This might add time, but it lets you check progress.
    #line.append(tract) # Add the tract to the end of the row list
    #csvwriter.writerow(line) # Write the new row to the new document
    csvwriter.writerow([str(tract)]) #or just write the tract number
    #print(tract); # print the tract for troubleshooting.
