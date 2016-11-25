# Jen Lamere
# 11/26/2016
import csv, math
import ast
import operator


datafile = "../Prototyping/prototypes.csv"

file = open("similarity.csv", 'wb')
writer = csv.writer(file, quoting=csv.QUOTE_ALL)

# calculated in build profile
attributes = ["Smooth &amp; Supple",
"Big &amp; Bold",
"Rich &amp; Creamy",
"Fruity &amp; Smooth",
"Earthy &amp; Spicy",
"Light &amp; Fruity",
"Light &amp; Crisp",
]

# takes prototype and converts into vector
def make_vector(wine):
    vector = [0 for i in range(len(attributes) + 1)]
    for key, value in wine["Attributes"].iteritems():
        vector[attributes.index(key)] = float(value)/float(wine["Count"])
    return vector

# read in data file
with open(datafile, 'rb') as f:
    reader = csv.reader(f)
    raw_data = list(reader)
    for i, row_i in enumerate(raw_data):
        wine1 = row_i[0]
        data1 = ast.literal_eval(row_i[1])
        vector1 = make_vector(data1)

        # calculate the similarity between one wine and all wines
        for j, row_j in enumerate(raw_data):
            wine2 = row_j[0]
            data2 = ast.literal_eval(row_j[1])

            # if they are the same wine, ignore
            if wine1 == wine2:
                continue

            vector2 = make_vector(data2)

            # Euclidean Distance
            sumation = 0
            for i,v in enumerate(vector1):
                sumation += math.pow(v - vector2[i], 2)
            sumation = math.sqrt(sumation)

            # factor in if they are the same type of wine (red, white, etc)
            similarity = 1 if  data1["WineType"].keys() == data2["WineType"].keys() else 0
            similarity = (sumation + similarity) / 2
            writer.writerow([wine1 + "," + wine2 + "," + str(similarity)])

      
