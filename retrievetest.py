#!/usr/bin/python

import facebook, requests

def get_fb_token(app_id, app_secret):
    payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    #print file.text #to test what the FB api responded with    
    result = file.text.split("=")[1]
    #print result #to test the TOKEN
    return result

access_token=get_fb_token(1749981128573326,'f48d2715f97244d8ece9f3337de25a08')
graph=facebook.GraphAPI(access_token, version='2.6')
grupo=graph.get_connections(id='1593568867531347', connection_name='feed')

basedir='/home/rodrigo/py/10jan/'
basedate=open(basedir+'newlinksFound.txt').readline().strip()
newdate=basedate
allposts = []
repetidos=0
args = {'fields' : 'link', }
#log=open(basedir+'newlinksFound.log','w')
class Found(Exception): pass

# Wrap this block in a while loop so we can keep paginating requests until
# finished.
while(True):
        for post in grupo['data']:
            try:
                if graph.get_object(post['id'], fields='type')['type'].encode('utf-8') == 'video':
                    print graph.get_object(post['id'], **args)['link'].encode('utf-8')
                    '''
                    if graph.get_object(post['id'], fields='created_time')['created_time'] > basedate:
                    #if graph.get_object(post['id'], **args)['link'].encode('utf-8') not in open(basedir+'newlinksFound.txt').read().splitlines():
                        allposts.append(graph.get_object(post['id'], **args)['link'].encode('utf-8'))
                        if graph.get_object(post['id'], fields='created_time')['created_time'] > newdate:
                            newdate=graph.get_object(post['id'], fields='created_time')['created_time']
                    else:
                        repetidos += 1
                    '''
            except:
                #log.write(str(e)+'\n')
                break
