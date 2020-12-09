import ryan_geocoder

coder = ryan_geocoder.RyanGeocoder()

longs, lats = coder.load_long_lats("C:\\Users\\ladav\\Downloads\\BPD_Part_1_Victim_Based_Crime_Data.csv")


for i in range(len(longs)):
    tract = coder.get_tract(longs[i+1], lats[i+1])
    print(tract)