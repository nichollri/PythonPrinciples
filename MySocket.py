import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

find_items = {'Date':'Date:\s(.+)', 'Etag':"ETag:\s(.+)"}
# write data to a file
fout = open('receive_data.txt', 'w')
output_str = ""
while True:
    data = mysock.recv(512)
    data_str = str(data)
    #data = data.rstrip()
    if ( len(data) < 1 ) :
        break
    for key in find_items:
        reg_ex = find_items[key]
        print "key:", key
        mymatch = re.findall(reg_ex, data)
        # returns a list of matched strings
        if len(mymatch) != 0:
            for item in mymatch:
                output_str = output_str + key + ": " + str(item) + "\n"
    print data;
    fout.write(data)
print "Output String:", output_str
mysock.close()
fout.close()
