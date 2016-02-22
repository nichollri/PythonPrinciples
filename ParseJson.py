import urllib
import json


address = raw_input('Enter location:')
uh = urllib.urlopen(address)
data = uh.read()
json_stuff = json.loads(data)

comm_array = json_stuff["comments"]
print type(comm_array)

total = 0
for comment in comm_array:
    count_str = comment["count"]
    total += int(count_str)

print total
