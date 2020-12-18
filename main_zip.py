import ryan_geocoder
import csv

coder = ryan_geocoder.RyanGeocoder()

#longs, lats = coder.load_long_lats("BPD_Part_1_Victim_Based_Crime_Data.csv")
#longs, lats = coder.load_long_lats("Crime Data Honors.csv")
longs = []
lats = []
oldfile = open('Crime Data Honors Filtered.csv', 'r');
csvreader = csv.reader(oldfile, delimiter=',');
newfile = open('Crime Data Honors Output.csv', 'w', newline='');
csvwriter = csv.writer(newfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

for line in csvreader:
    long=line[10]
    lat=line[11]
    tract = coder.get_tract(long, lat)
    #csvwriter.writerow((line, tract))
    newfile.flush()
    line.append(tract)
    csvwriter.writerow(line)

    #print(tract)


'''for i in range(len(longs)):
    tract = coder.get_tract(longs[i+1], lats[i+1])
    print(tract)'''