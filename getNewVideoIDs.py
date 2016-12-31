#!/usr/bin/python3
import re
import datetime
import os

basedir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '')

regex=r'(youtu\.be\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v)\/|attribution_link\?a=))(.+)'
'''
Posibles matches:
youtu.be/[ID]
youtube.com/watch?v=[ID]
youtube.com/embed/[ID]
youtube.com/v/[ID]
youtube.com/attribution_link?a=[ID]
'''

cant=0
file=open(basedir+'videoIDs.txt','w')
with open(basedir+'newlinksFound.txt') as links:
    contenido=links.read()
    links.close()
for elem in contenido.splitlines():
    i=re.split(regex, elem)
    try:
        id=i[-2]
        #print(id)
        if id.find(r'%3D')!=-1:
            #print(id)
            id=id[id.find('%3D')+3:]
            #print(id)
            id=id[:id.find('%')]
            #print(id)
        elif id.find('&'):
            id=id[:id.find('&')]
        file.write(id + '\n')
        cant+=1
    except:
        pass
file.close()
print('Links de Youtube: ' + str(cant))
