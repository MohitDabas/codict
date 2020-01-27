import json
import re
import requests
with open('phplangdb.json') as fp:
    data =json.load(fp)
def phpsendSuggestion(functionName):
    global data
    tenSuggestion=[]
    for i in range(0,len(data[1]['entries'])):
     if ( re.findall(r'{0}'.format(functionName), data[1]['entries'][i]['name'], re.IGNORECASE)):
        tempDict={}
        tempDict['functionName']=data[1]['entries'][i]['name']
        tempDict['path']=data[1]['entries'][i]['path']
        tempDict['type']=data[1]['entries'][i]['type']
        tenSuggestion.append(tempDict)
    return tenSuggestion[0:20] 

def phpDescribeRequest(functionName,path):
    headers = {
    'authority': 'docs.devdocs.io',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8,lb;q=0.7',
}

    
    path=path.split('#')[0]+'.html'
    print('https://docs.devdocs.io/php/'+path)
    response = requests.get('https://docs.devdocs.io/php/'+path, 
    headers=headers)
    data=response.text
    indexOfRefname=data.find('<div class="refnamediv">') 
    indexOfExample=data.find('<h3 class="title">Examples</h3>',indexOfRefname)
    return data[indexOfRefname:indexOfExample]
           