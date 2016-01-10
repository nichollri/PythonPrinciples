from BeautifulSoup import *
import urllib2

#test_url = "http://python-data.dr-chuck.net/comments_42.html"
test_url = " http://python-data.dr-chuck.net/comments_216724.html"
#test_url = " http://www.cnn.com"

#extract the html
html_fh = urllib2.urlopen(test_url)
my_html = html_fh.read()

soup = BeautifulSoup(my_html)

print "Soup:", soup, ":Soup"
my_span_tags = soup('span')

total = 0
for html_tag in my_span_tags:
    tag_content = html_tag.contents[0]
    print tag_content
    #print type(tag_content)
    total += int(tag_content)
    #print total

print "The final total is: ", total
