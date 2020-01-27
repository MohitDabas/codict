import json
import re
import requests
with open('nodejslangdb.json') as fp:
    data =json.load(fp)
def nodejssendSuggestion(functionName):
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

def nodejsDescribeRequest(functionName,path):
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

    
  
    print('https://docs.devdocs.io/node/'+path.split('#')[0]+'.html')
    response = requests.get('https://docs.devdocs.io/node/'+path.split('#')[0]+'.html', 
    headers=headers)
    data=response.text
    indexOfRefname=data.find('<h3 id="{}">'.format(path.split('#')[1])) 
    indexOfExample=data.find('<h3 id="',indexOfRefname+15)
    print (indexOfRefname,indexOfExample)
    print('<h3 id="{}">'.format(path.split('#')[1]))
    if (indexOfRefname==-1 or indexOfExample==-1):
        indexOfRefname=data.find('<h2 id="{}">'.format(path.split('#')[1])) 
        indexOfExample=data.find('<h2 id="',indexOfRefname+15)
    if (indexOfRefname==-1 or indexOfExample==-1):
        indexOfRefname=data.find('<h4 id="{}">'.format(path.split('#')[1])) 
        indexOfExample=data.find('<h4 id="',indexOfRefname+15)    
        
    return data[indexOfRefname:indexOfExample]     