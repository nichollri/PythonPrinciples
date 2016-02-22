import urllib
import xml.etree.ElementTree as ET


url = raw_input('Enter location: ')
#http://python-data.dr-chuck.net/comments_42.xml
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)
comment_info_node = tree.findall('comments/comment')
total = 0
for each_comment in comment_info_node:
    count_str = each_comment.find('count').text
    count = int(count_str)
    total += count

print "The total is:", total



    #results = tree.findall('result')
    #lat = results[0].find('geometry').find('location').find('lat').text
    #lng = results[0].find('geometry').find('location').find('lng').text
    #location = results[0].find('formatted_address').text
