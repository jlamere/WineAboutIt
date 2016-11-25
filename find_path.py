# Jen Lamere
# 11/25/2016

import matplotlib as mpl
mpl.use('Agg')
import networkx as nx
import csv, ast
import matplotlib.pyplot as plt

# Two graphs: one with seven edges per node and one with 5
G_strong = nx.Graph()
G_weak = nx.Graph()

# read in prototype data to give user once path is found
wines = {}
datafile = "./Prototyping/prototypes.csv"
with open(datafile, 'rb') as f:
    reader = csv.reader(f)
    raw_data = list(reader)
    for i in raw_data:
        wines[i[0]] = ast.literal_eval(i[1])

# read in edge data
datafile = "./Similarity/similarity_weak.csv"
with open(datafile, 'rb') as f:
    reader = csv.reader(f)
    raw_data = list(reader)
    for i,r in enumerate(raw_data):
        row = r[0].split(',')
        # Populate both strong and weak graphs
        if(i <5):
            G_weak.add_edge(row[0], row[1], weight=row[2])
        G_strong.add_edge(row[0], row[1], weight=row[2])


# Get wine info from users
print("Select two wines to try: ")
for w in wines:
        print w

wine1 = ""
while wine1 not in wines:
    wine1 = raw_input('Enter your favorite wine: ').strip()

wine2 = ""
while wine2 not in wines:
    wine2 = raw_input("Enter wine you want to try: ").strip()

# Find the path
path = []
try:
    path = nx.shortest_path(G_strong,wine1,wine2)
    print("Strong path found")
except:
    path = nx.shortest_path(G_weak,wine1,wine2)
    print("Weak path found")

# Print out information on the path (such as characteristics of the wine)
for p in path:
    print " "

    print p
    print wines[p]["WineType"].keys()[0]
    for a in wines[p]["Attributes"]:
        print a.replace("&amp", ""),
    print " "
