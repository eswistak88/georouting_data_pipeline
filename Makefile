net := outputs/BursaScenario.net.xml
poly := outputs/BursaScenario.poly.xml
trace := outputs/trace.txt
route := outputs/BursaScenario.rou.xml
code_snippets := outputs/code_snippets.txt

all: $(route) $(poly) $(code_snippets)

.PHONY: route
route: $(route)
$(route): $(trace)
	python $(SUMO_HOME)/tools/route/tracemapper.py -n outputs/BursaScenario.net.xml -t outputs/trace.txt -o outputs/BursaScenario.rou.xml --geo
	python src/update_start_times.py
	duarouter --route-files outputs/BursaScenario.rou.xml --net-file outputs/BursaScenario.net.xml -o outputs/BursaScenario.rou.xml --repair --ignore-errors

.PHONY: poly
poly: $(poly)
$(poly): clientFiles/BursaScenario.osm.xml net
	polyconvert --net-file outputs/BursaScenario.net.xml --osm-files clientFiles/BursaScenario.osm.xml --osm.keep-full-type false --output-file outputs/BursaScenario.poly.xml

.PHONY: code_snippets
code_snippets: $(code_snippets)
$(code_snippets): net
	python3 src/LonLat2TraciCoord.py

.PHONY: trace
trace: $(trace)
$(trace): $(net)
	python3 src/convert_csv_to_trace.py

.PHONY: net
net: $(net)
$(net):
	netconvert --configuration-file src/config/BursaScenario.netccfg --osm-files clientFiles/BursaScenario.osm.xml --output-file outputs/BursaScenario.net.xml




