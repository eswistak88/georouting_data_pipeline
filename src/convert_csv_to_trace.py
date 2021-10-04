import os, sys
if 'SUMO_HOME' in os.environ:
	tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
	sys.path.append(tools)
else:
	sys.exit("please declare environment variable 'SUMO_HOME'")
import pandas as pd
import re
import pickle



def convert_csv_trace_to_sumo_trace():
	os.chdir("/home/eswistak/drive")
	with open('outputs/BursaScenario.net.xml', 'r') as f:
		for line in f.readlines():
			boundaries = re.match(r'\s+\<location.*origBoundary="(\d+\.\d+),(\d+\.\d+),(\d+\.\d+),(\d+\.\d+)', line)
			if boundaries:
				break
	beg_lon, beg_lat, end_lon, end_lat = boundaries.groups()
	beg_lon, beg_lat, end_lon, end_lat = float(beg_lon), float(beg_lat), float(end_lon), float(end_lat)
	header = ['Id', 'timestamp', 'distance', 'speed', 'LonLats']
	csv_trace = pd.read_csv("clientFiles/bursa1original.csv", names=header, parse_dates=[1])
	print("Imported csv trace file")
	csv_trace.sort_values(by='timestamp')
	first_time = csv_trace.iloc[0]['timestamp']
	coords = {}
	start_times = {}
	for _i,trace in csv_trace.iterrows():
		if trace['Id'] not in coords.keys():
			coords[trace['Id']] = []
			start_times[trace['Id']] = (trace['timestamp'] - first_time).total_seconds()
		LonLats = trace['LonLats']
		LonLats = [lonlat.replace(" ", ",") for lonlat in LonLats[LonLats.index('(') + 1:LonLats.index(')')].split(',')]
		coords[trace['Id']].extend(LonLats)
		if(_i > 0 and _i %100000 == 0):
			print("Completed {} traces".format(_i))
	trace_string = ""
	for key in coords.keys():
		clean_coords = []
		for coord in coords[key]:
			coord = coord.split(",")
			lon = float(coord[0])
			lat = float(coord[1])
			if(lon > beg_lon and lon < end_lon and lat > beg_lat and lat < end_lat):
				clean_coords.append(str(lon) + "," + str(lat))
		trace_string += (str(key) + ":" + " ".join(clean_coords) + "\n")
	with open("outputs/trace.txt", 'w+') as file:
		file.write(trace_string)
	with open('outputs/start_times.pkl', 'wb+') as file:
		pickle.dump(start_times, file)

if __name__=="__main__":
	convert_csv_trace_to_sumo_trace()