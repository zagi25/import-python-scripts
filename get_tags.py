import requests
import json
from urllib.parse import urlparse

cookies = {'login-token': 'fd628a0f-843a-414a-924a-834884b8fa25%3addb9beb7-6fc3-4d64-853f-71c783b7148c_8afc6adb9ef476f0706b68da4969f9ca%3acrx.default'}
BASE_URL = 'https://dc-author.corp.adobe.com/content/dx-dc/us/en'
URL_SUF = '/jcr:content.json'

tags = {};
with open('pages.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        try: 
            parsedUrl = urlparse(line);
            path = parsedUrl.path.split('.')[0]
            req = requests.get(BASE_URL + path + URL_SUF, cookies=cookies)
            data = req.json()
            tags[line.rstrip()] = data['cq:tags']
            print(line.rstrip() + ' success')
        except:
            print(line.rstrip() + ' fail')

json_string = json.dumps(tags)
with open('caas_tags.json', 'w') as outfile:
    outfile.write(json_string)

print('Done')
