import os, sys
if 'SUMO_HOME' in os.environ:
	tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
	sys.path.append(tools)
else:
	sys.exit("please declare environment variable 'SUMO_HOME'")

import sumolib

import csv

net = sumolib.net.readNet('outputs/BursaScenario.net.xml')

with open('clientFiles/POIs.csv', 'r') as csv_file:
	reader = csv.reader(csv_file)
	coords = []
	for row in reader:
		coords.append([row[1],row[2]])

coords = coords[1:]
code_snippet = "TraCICoord TraciPOIcoords[16] = {"
for row in coords:
	x, y = net.convertLonLat2XY(row[0],row[1])
	code_snippet += "TraCICoord(" + str(x) + "," + str(y) + "),\n"
code_snippet = code_snippet[:-2] + "};\n\n\n"

xmin, ymin, xmax, ymax = net.getBoundary()
for i, row in enumerate(coords):
	x, y = net.convertLonLat2XY(row[0],row[1])
	code_snippet += "*.rsu[" + str(i) + "].mobility.x = " + str(x) + "\n"
	code_snippet += "*.rsu[" + str(i) + "].mobility.y = " + str(ymax - y - 1147.0) + "\n"
with open('outputs/code_snippets.txt', "w+") as f:
	f.write(code_snippet)