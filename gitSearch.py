import requests
from curlparser import parse
def codesearch(lang, functionName):
    fOpen=open('curlCommand.txt')
    fileData=fOpen.read()
    fOpen.close()
    result=parse(fileData)
    print (result['headers'])
    print(result['cookies'])
    cookies =result['cookies']

    headers =result['headers']
    params = (
        ('l', lang),
        ('q', functionName),
        ('type', 'Code'),
    )

    response = requests.get('https://github.com/search',
                            headers=headers, params=params, cookies=cookies)
    data = response.text
    print(response.url)
    indexOfStart = data.find('<div id="code_search_results">')
    indexOfEnd = data.find(
        '<div class="paginate-container codesearch-pagination-container">', indexOfStart)

    # print(data[indexOfStart:indexOfEnd])
    return data[indexOfStart:indexOfEnd]
