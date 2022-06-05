import socket
import sys
from plot import *
from getloc import *
from trace import traceroute
from help import *

# get hostname from parse
if len(sys.argv)<2:
    printHelp()
    exit()
    
hostname = sys.argv[1]

# get my location (myIP,(lon,lat),city)
myLoc = getMyLoc()


# get target location IP,(lon,lat),city
targetIP = socket.gethostbyname(hostname)
targetLoc = getTargetLoc(targetIP)

# traceroute process to hostname and output the ipList : (ipAddress,(lon,lat),city)
ipList = traceroute(hostname)

# get geo location of the ipList and insert myLoc and TargetLoc
routeLocList = getLoc(ipList)
routeLocList.insert(0,myLoc)
routeLocList.append(targetLoc)

# prepare for and linear route in map
routeLocLon =[]
routeLocLat = []
tempLon = 0
tempLat = 0
for x in routeLocList:
    # this looping will drop the route that have zero movement
    if x[1][0]-tempLon == 0 or x[1][1]-tempLat == 0:
        continue
    routeLocLon.append(x[1][0])
    routeLocLat.append(x[1][1])

    tempLon = x[1][0]
    tempLat = x[1][1]


# initiate the maps
fig = go.Figure()
mapsInit(fig)

# creating the route
for i in range(len(routeLocLon)-1):
    for x in routeLocList:
        if (routeLocLon[i],routeLocLat[i]) in x:
            route_city = x[2]
            route_ip = x[0]
    print(route_ip,'---',route_city)
    addRoute(fig,f'route{i}',((routeLocLon[i:i+2],routeLocLat[i:i+2]),route_city))
print(targetLoc[0],'---',targetLoc[2])

# marking the source IP and destination IP
mark(fig,f'My IP - {myLoc[2]}', myLoc[1])
mark(fig,f'{hostname} - {targetLoc[2]}',targetLoc[1],name=hostname)

fig.show()

