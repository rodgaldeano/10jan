#/usr/bin/python

import facebook, requests

def get_fb_token(app_id, app_secret):
    payload = {'grant_type': 'client_credentials','client_id': app_id, 'client_secret': app_secret}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    result=file.text.split(':')[1].split(',')[0]#to test what the FB api responded with    
    result=result[1:len(result)-1]
    #print result #to test the TOKEN
    print result
    return result

access_token=get_fb_token(1749981128573326,'f48d2715f97244d8ece9f3337de25a08')
graph=facebook.GraphAPI(access_token, version='2.6')
grupo=graph.get_connections(id='1593568867531347', connection_name='feed')

allposts = []
args = {'fields' : 'link', }
log=open('linksFound.log','w')

# Wrap this block in a while loop so we can keep paginating requests until
# finished.
while(True):
    try:
        for post in grupo['data']:
            try:
                allposts.append(graph.get_object(post['id'], **args)['link'].encode('utf-8'))
            except Exception as e:
                log.write(str(e) + '\n')
        # Attempt to make a request to the next page of data, if it exists.
        grupo=requests.get(grupo['paging']['next']).json()
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
        break
file=open('linksFound.txt','w')
for i in allposts:
    file.write(i + '\n')
file.close()
log.close()
