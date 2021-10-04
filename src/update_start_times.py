import xml.dom.minidom as dom
from xml import parsers
import pickle

route = dom.parse('outputs/BursaScenario.rou.xml')

routes = route.childNodes[1]

with open('outputs/start_times.pkl', 'rb') as f: 
    start_times = pickle.load(f)

for element in route.getElementsByTagName("route"):
    vehicle = route.createElement("vehicle")
    vehicle.setAttribute("id", element.getAttribute("id"))
    vehicle.setAttribute("depart", str(start_times[int(element.getAttribute("id"))]))
    element.removeAttribute("id")
    vehicle.appendChild(element.cloneNode(True))
    routes.replaceChild(vehicle, element)


with open('outputs/BursaScenario.rou.xml', 'w') as f:
    route.writexml(f)