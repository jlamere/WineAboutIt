# Jen Lamere
# 11/25/2016

import requests, csv
from api_key import key
from attributes import attributes

categories = []
categories_str = ""
offset = 0
size = 10
file = open("raw_data.csv", 'wb')
wr = csv.writer(file, quoting=csv.QUOTE_ALL)


# pull in attributes to query on
def build_categories():
    for attribute in attributes:
        datafile = "./Attributes" + attribute + ".csv"
        with open(datafile, 'rb') as f:
            reader = csv.reader(f)
            raw_data = list(reader)
            categories.extend([r[0].split(',')[1] for r in raw_data])

# query wine API for wine matching categories
def get_data():
    url = base_url + "/catalog?filter=(490+%s)&offset=%s&size=%s&apikey=%s" % (categories_str, offset*size, size, key)
    resp = requests.get(url)
    jsonResponse = resp.json()
    wr.writerow(jsonResponse['Products']['List'])


build_categories()
categories_str = '|'.join(categories)
base_url = "http://services.wine.com/api/beta2/service.svc/json"

# query 10,000 wines
while(offset < 1000):
    print offset * size
    get_data()
    offset+=1
