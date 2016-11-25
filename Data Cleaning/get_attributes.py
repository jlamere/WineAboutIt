import requests, csv
from api_key import key
from attributes import attributes


base_url = "http://services.wine.com/api/beta2/service.svc/json/"
url = base_url + "categorymap?filter=categories(490)&apikey=" + key
print url

resp = requests.get(url)
if resp.status_code != 200:
    raise ApiError('GET /catalog/ {}'.format(resp.status_code))

jsonResponse = resp.json()

for header in jsonResponse['Categories']:
    if header['Name'] in attributes:
        file = open(header['Name'] + ".csv", 'wb')
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        for r in header["Refinements"]:
            row = r['Name'].replace(',', '') + ',' + str(r["Id"])
            print(row)
            wr.writerow([row.encode('utf-8')])
