import csv, math, heapq,ast
from operator import itemgetter


datafile = "./similarity.csv"
file_strong = open("similarity_strong.csv", 'wb')
file_weak = open("similarity_weak.csv", 'wb')
writer_strong = csv.writer(file_strong, quoting=csv.QUOTE_ALL)
writer_weak = csv.writer(file_weak, quoting=csv.QUOTE_ALL)


data = {}
with open(datafile, 'rb') as f:
    reader = csv.reader(f)
    raw_data = list(reader)
    for r in raw_data:
        row =r[0].split(',')
        if row[0] not in data:
            data[row[0]] = [(row[1], row[2])]
        else:
            data[row[0]].append((row[1], row[2]))

for k,v in data.iteritems():
    v.sort(key=itemgetter(1), reverse=True)
    final_attr_strong = v[:5]
    for a in final_attr_strong:
        writer_strong.writerow([k + "," + a[0] + "," + str(a[1])])
    final_attr_weak = v[:7]
    for a in final_attr_weak:
        writer_weak.writerow([k + "," + a[0] + "," + str(a[1])])
