import urllib
import json


place = raw_input('Enter place:')
address = 'http://python-data.dr-chuck.net/geojson?'
url = address + urllib.urlencode({'sensor':'false', 'address':place})
print url
uh = urllib.urlopen(url)

data = uh.read()
json_stuff = json.loads(data)
#print json.dumps(json_stuff)
fout = open('place_id.txt', 'w')

result_array = json_stuff['results']
print type(result_array)
for result in result_array:
    print type(result)
    print result.keys()
    print result['place_id']
    fout.write(result['place_id'])
