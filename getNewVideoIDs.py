#!/usr/bin/python3
import re
import datetime
import os

basedir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '')

regex=r'(youtu\.be\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v)\/|attribution_link\?a=))'
cant=0
file=open(basedir+'videoIDs.txt','w')
#file.write(str(datetime.datetime.now()) + '\n')
with open(basedir+'newlinksFound.txt') as links:
    contenido=links.read()
    links.close()
for elem in contenido.splitlines():
    i=re.split(regex, elem)
    try:
        id=i[-2]
        if id.find('http')!=-1:
            id=id[:id.find('http')]
        file.write(id + '\n')
        cant+=1
    except:
        pass
file.close()
print('Links de Youtube: ' + str(cant))
