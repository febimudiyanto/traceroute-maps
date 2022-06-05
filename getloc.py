import ipaddress
import json
import requests

def getMyLoc():
    '''
    return: MyIP, lon,lat,city
    '''
    url = 'https://ipapi.co/json/'
    response = requests.get(url)
    data = response.json()
    try:
        myIP = data['ip']
        lon =data['longitude']
        lat = data['latitude']
        city = data['city']
    except KeyError as a:
        print(f'Error: {a} Not Found')
        exit()

    return (myIP,(lon,lat),city)

def getTargetLoc(IP):
    '''
    input: IP
    return: lon,lat,city
    '''
    url = f'https://ipapi.co/{IP}/json/'
    response = requests.get(url)
    data = response.json()
    try:
        lon =data['longitude']
        lat = data['latitude']
        city = data['city']
    except KeyError as a:
        print(f'Error: {a} Not Found')
        exit()

    return (IP,(lon,lat),city)



def getLoc(ipList):
    '''
    input: (tuple/list)--> ipAddress
    output: (List) (ipAddress,longitude, latitude, city)
    '''
    List = []
    for ipAddress in ipList:
        url = f'https://ipapi.co/{ipAddress}/json/'
        response = requests.get(url)
        data = response.json()
        
        # cek if IP is private ip
        try:
            if data['error'] == True:
                continue
        except KeyError:
            pass

        
        lon =data['longitude']
        lat = data['latitude']
        if lon == None or lat == None:
            continue
        city = data['city']
        List.append((ipAddress,(lon,lat),city))

    return List