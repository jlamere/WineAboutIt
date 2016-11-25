import csv
import ast


datafile = "./../Data Cleaning/clean_data.csv"
wine_types = {}
wine_attributes = []

file = open("attributes.csv", 'wb')
a_writer = csv.writer(file, quoting=csv.QUOTE_ALL)

def new_wine_type(wine):
    attributes = {}
    for a in wine["Attibutes"]:
        if a not in wine_attributes:
            wine_attributes.append(a)
            a_writer.writerow([a])
        attributes[a] = 1
    wine_types[wine['Type']] = {}
    wine_types[wine['Type']]["Attributes"] = attributes
    wine_types[wine['Type']]["WineType"] = { wine["WineType"] : 1}
    wine_types[wine['Type']]["Count"] = 1



def existing_wine_type(wine):
    for a in wine["Attibutes"]:
        if a not in wine_attributes:
            wine_attributes.append(a)
            a_writer.writerow([a])

        if a in wine_types[wine['Type']]["Attributes"]:
            wine_types[wine['Type']]["Attributes"][a] += 1
        else:
            wine_types[wine['Type']]["Attributes"][a] = 1

    if wine["WineType"] in wine_types[wine['Type']]["WineType"]:
        wine_types[wine['Type']]["WineType"][wine["WineType"]] +=  1
    else:
        wine_types[wine['Type']]["WineType"][wine["WineType"]] = 1
    wine_types[wine['Type']]["Count"] += 1


with open(datafile, 'rb') as f:
    reader = csv.reader(f)
    raw_data = list(reader)
    for i in raw_data:
        for j in i:
            wine = ast.literal_eval(j)
            if(wine["Type"] in wine_types):
                existing_wine_type(wine)
            else:
                new_wine_type(wine)

file = open("prototypes.csv", 'wb')
wr = csv.writer(file, quoting=csv.QUOTE_ALL)
for key, value in wine_types.iteritems():
    wr.writerow([key.encode('utf-8'), value])
