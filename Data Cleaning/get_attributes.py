# Jen Lamere
# 11/25/2016

import requests, csv
from api_key import key
from attributes import attributes

# building url
base_url = "http://services.wine.com/api/beta2/service.svc/json/"
url = base_url + "categorymap?filter=categories(490)&apikey=" + key

resp = requests.get(url)
jsonResponse = resp.json()

# find all attributes stored on wine
for header in jsonResponse['Categories']:
    if header['Name'] in attributes:
        file = open(header['Name'] + ".csv", 'wb')
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        for r in header["Refinements"]:
            row = r['Name'].replace(',', '') + ',' + str(r["Id"])
            print(row)
            wr.writerow([row.encode('utf-8')])
