from BeautifulSoup import *
import urllib2

#found_href = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html"
found_href = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Kenan.html"
#found_href = " http://www.yahoo.com"
line_to_find = 18
repeat = 7

def find_href(href_tags, line_to_find):
    count = 0
    for tag in href_tags:
        next_href = tag.get('href', None)
        count+=1
        if (count == line_to_find):
            break

    return (next_href)


for i in range(1,repeat+1):
    html_fh = urllib2.urlopen(found_href)
    my_html = html_fh.read()
    soup = BeautifulSoup(my_html)
    href_tags = soup("a")
    found_href = find_href(href_tags, line_to_find)
    print found_href

print "final:", found_href
