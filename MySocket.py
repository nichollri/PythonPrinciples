import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

# write data to a file
fout = open('receive_data.txt', 'w')
output_str = ""
while True:
    data = mysock.recv(512)
    data_str = str(data)
    #data = data.rstrip()
    if ( len(data) < 1 ) :
        break
    mydate = re.findall('Date:\s(.+)', data)
    mywhy = re.findall('Why\s(.+)', data_str)
    if len(mydate) != 0:
        for item in mydate:
            output_str = output_str + str(item)
    print data;
    fout.write(data)
print output_str
mysock.close()
fout.close()
