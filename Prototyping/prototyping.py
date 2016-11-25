# Jen Lamere
# 11/25/2016
import csv
import ast
import operator


datafile = "./prototypes.csv"
# Read in attributes, and print out data better formatted
with open(datafile, 'rb') as f:
    reader = csv.reader(f)
    raw_data = list(reader)
    for row in raw_data:
        wine = row[0]
        data = ast.literal_eval(row[1])
      
        print wine
        for a in data["Attributes"]:
            print "\t" + a + " " + str(data["Attributes"][a]) + " " + str(float(data["Attributes"][a])/float(data["Count"]))