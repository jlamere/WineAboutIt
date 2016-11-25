# Jen Lamere
# 11/25/2016
import csv
import ast

wine_type= {}

# write out clean data
file = open("clean_data.csv", 'wb')
clean_data_file = csv.writer(file, quoting=csv.QUOTE_ALL)

# write out different wine types & quantities
file = open("wine_types.csv", 'wb')
wine_type_file = csv.writer(file, quoting=csv.QUOTE_ALL)

# Only store attributes that will be relevant for similarities
# Discard any data points with missing data
def clean_wine(one_wine):
    # skip wine with missing data
    if (one_wine["Varietal"] == None) or (one_wine["Type"] != "Wine") or (one_wine["ProductAttributes"] == None):
        return

    wine_clean = {}
    wine_clean["Attibutes"] = [r["Name"] for r in one_wine["ProductAttributes"] if r["Id"] in xrange(610, 617)]
    wine_clean['Name'] = one_wine['Name']
    wine_clean['Type'] = one_wine["Varietal"]["Name"]
    wine_clean['WineType'] = one_wine["Varietal"]["WineType"]["Name"]
    exists = one_wine["Varietal"]["Name"] in wine_type
    wine_type[one_wine["Varietal"]["Name"]] = wine_type[one_wine["Varietal"]["Name"]] + 1 if exists else 1
    clean_data_file.writerow([wine_clean])

datafile = "raw_data.csv"
with open(datafile, 'rb') as f:
    reader = csv.reader(f)
    raw_data = list(reader)
    for i in raw_data:
        for j in i:
            clean_wine(ast.literal_eval(j))


for key, val in wine_type.items():
    wine_type_file.writerow([key.encode('utf-8'), val])