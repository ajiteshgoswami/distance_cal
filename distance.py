import urllib.request, urllib.parse, urllib.error
import json
import ssl
from math import sin, cos, sqrt, atan2, radians

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location 1: ')


parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
    

print(json.dumps(js, indent=4))
lat1 = radians(js["results"][0]["geometry"]["location"]["lat"])
lon1 = radians(js["results"][0]["geometry"]["location"]["lng"])
print("Lat 1 = ", lat1)
print("Lon 1 = ", lon1)


address = input('Enter location 2: ')


parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None
if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
    

print(json.dumps(js, indent=4))
lat2 = radians(js["results"][0]["geometry"]["location"]["lat"])
lon2 = radians(js["results"][0]["geometry"]["location"]["lng"])
print("Lat 1 = ", lat1)
print("Lon 1 = ", lon1)
print("Lat 2 = ", lat2)
print("Lon 2 = ", lon2)

R = 6373.0
dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Result:", distance)


