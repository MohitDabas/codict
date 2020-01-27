import json
import re
import requests
with open('pythonlangdb.json') as fp:
    data =json.load(fp)
def pythonsendSuggestion(functionName):
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

def pythonDescribeRequest(functionName,path):
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

    
    urlPath=path.split('#')[0]+'.html'
    print('https://docs.devdocs.io/python~3.7/'+urlPath)
    response = requests.get('https://docs.devdocs.io/python~3.7/'+urlPath, 
    headers=headers)
   # if '()' in functionName:
        #functionName=functionName.replace('.','\.')
   #     functionName=functionName.replace('()','\(.*\)')
   # print (functionName.count('.'))
   # if functionName.count('.')==3:
   #     print (functionName.split('.'))
   #     functionName=functionName.split('.')[1]+'.'+functionName.split('.')[2]
   
       

    

    data=response.text
    print(path,'<dt id="{}">'.format(path.split('#')[1]))
    indexOfStart=data.find('<dt id="{}">'.format(path.split('#')[1])) 
    indexOfEnd=data.find('</dl>',indexOfStart)   
    print(indexOfEnd,indexOfStart)
    return data[indexOfStart:indexOfEnd]

    #print (data)
    #regex=r'<dt id="{}">.*'.format(path.split('#')[1])
    #print (regex)
    #matches = re.finditer(regex, data, re.MULTILINE | re.VERBOSE )
    #if (len(list(matches))==0):
    #    return "No Description"

   # for matchNum, match in enumerate(matches, start=1):       
   #   print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
   #   start = match.start()
   #   print(type(start))
   #   indexOfDl=data[start:].find('</dl>')
   #   print (indexOfDl)
   #   print(data[start:start+indexOfDl])
   #   print(len(data[start:start+indexOfDl]))
   #   return data[start:start+indexOfDl]
   
        
        #print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
       

#describeRequest('os.tcgetpgrp()','library/os#os.system')    
    

    