# Jen Lamere
# 11/25/2016
# Reads in all different wines, and comes up with a prototype based off of each wine type (such as Pinot Noir)

import csv
import ast


wine_types = {}
wine_attributes = []

# store all possible attributes
file = open("attributes.csv", 'wb')
a_writer = csv.writer(file, quoting=csv.QUOTE_ALL)

# if first type of wine being stored
def new_wine_type(wine):
    attributes = {}
    wine_type = wine["Type"]
    # gather all wine attributes
    for a in wine["Attibutes"]:
        if a not in wine_attributes:
            wine_attributes.append(a)
            a_writer.writerow([a])
        attributes[a] = 1

    # store initial prototype of wine
    wine_types[wine_type] = {}
    wine_types[wine_type]["Attributes"] = attributes
    wine_types[wine_type]["WineType"] = { wine["WineType"] : 1}
    wine_types[wine_type]["Count"] = 1


# if wine already has a prototype, update it
def existing_wine_type(wine):
    # keep track of attributes
    for a in wine["Attibutes"]:
        if a not in wine_attributes:
            wine_attributes.append(a)
            a_writer.writerow([a])
        attributes =  wine_types[wine['Type']]["Attributes"]
        wine_types[wine['Type']]["Attributes"][a] = attributes[a] + 1 if a in attributes else 1

    wine_type = wine_types[wine['Type']]["WineType"]
    wine_type[wine["WineType"]] = wine_type[wine["WineType"]] + 1 if wine["WineType"] in wine_type else 1
    wine_types[wine['Type']]["Count"] += 1

# read in data
datafile = "./../Data Cleaning/clean_data.csv"
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

# write out wine type data
file = open("prototypes.csv", 'wb')
wr = csv.writer(file, quoting=csv.QUOTE_ALL)
for key, value in wine_types.iteritems():
    wr.writerow([key.encode('utf-8'), value])
