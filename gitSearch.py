import requests


def codesearch(lang, functionName):
    cookies = {
        '_ga': 'GA1.2.702421455.1508821525',
        '_device_id': 'c8713ace3c8ec140be1b7c4f44b0119c',
        'logged_in': 'yes',
        'dotcom_user': 'MohitDabas',
        '_octo': 'GH1.1.551049781.1568455973',
        'user_session': 'BCeUzYvA7e8g8u0IEiQbUX7bMlMWyKGgXFTcf59fCc3GHXoQ',
        '__Host-user_session_same_site': 'BCeUzYvA7e8g8u0IEiQbUX7bMlMWyKGgXFTcf59fCc3GHXoQ',
        'tz': 'Asia%2FCalcutta',
        'ignored_unsupported_browser_notice': 'false',
        'has_recent_activity': '1',
        '_gh_sess': 'YnF5TU5xaS9LOXRWTS9udkg4WGhjUUlnSmxHWEZPSm5XanpVMllaWldmV0dMa1FjeGlSMGYvUFRyMlp3ejZnSE5mdWxnVjVseXFIUlhhZ3lLTFI4ei81YTBWUDgzTmpKbGZXbXl4SDlkQ3VySjJ1QUIwU2dDK1ZiMVFBc0JJZDlBdVR2dTI4WWtQMURuMDdhUVFIOE91b3FveW5PZ0pyOE5qbU1YcmRtaXRtNlRoWlY1OUhJY0RkUlA5NXVQSVg0c0pzR01tM0VsTWtROS9IblZmTFZ0WHJOYTFQT2RlbzcwRTZqUVpNdEV6Z3J5bDE4LzgzT2ZlQnJibkNMdHU5ZnVLUFRsQVVtdmZvUmsrV0lDa3FJbjFlb1Nia2tqbG1sTnFIUk8zMjhZYjluaEh5T3AxY3JOSUI3QStpK2I0N1R6L1lob3htWE85b1NRR2VpdlE2SEthdVFTMkJObkZ5WUQwN2lXcHY2L3lCTEF5Rm1Tb2pXRk1jQzhhTnc2VlNlR2llMURYN2Y0REFwRmNYMmtWaVRIYzZxa3dIZUUzNTZJZFlWVzJEazYzQ0xCUmphUE5CRjQ3bmVPRHlQblJ5RVdrcm9RVXVlRU51amxrZzJvSFFiRmFKb3RUYlJucjVtMW5vR3U4MGRJWTdoOFRJSWt0eCt6bnZxdGdaMWNrampQTTJ0YVIyMlIwakRuMFZ5SjJNOHRhRitXcTFNdnplci9FR1N1KzR6N0w1NVRad0grRm1OV1FjNnZYOGJvSmY3QWt3QXRxelJvSmxTNTVTeUw1aE1VTnhDVEQrUW92RzMyRWw2RVpQUFZGZ2JSNTJBWm91aFA3bzdtWWJVL1ArdVIwSm9xNUptV3ZZY3ZOamJyVjhNS2ZrZ2U2Y2Q2aE94NHdMQnBqengrWnZWb1BpR0YrYXV1Z2lycFl4VDhjMFN3Vk9FYmVBQ3hlNDQzMGRsUzQ2eUNJOU11bWpCV01WY2xGdklGamVEM2RRaWNaNExSUVlHQ1JiOUpZSVlHSHNDS0M0aW1HV01xUENvaVI0cFRKMURrVTBDcnJLb2xRaFFkai9qSk40TlBjYjlZR0hZOFdvT0FYR1VkSHVGbTQ5dndlcllGb3dZNm5MUWp3ODVFb1lDbmhncDhVdk03Tk5IWEttcFFHQXgvVXdOTlBmWjhqV294cWFFdG40ajNZNzJhTnRrbW1oTVFIc015Wjl5SE5jL0VRcUNHZjVFd1JJYytYcXVsTW0yS3pWd0ord3V5VFFXZ0VJY3lJVklOK1NYS2V5ZnhsU0ViNVZSeldGUWtrWFNtSFVZNGdWeEJuRE5CaTZmU2Jxa251c1Jxb2hUbFgwYVMrRnZDdzU2VTdLcnJCTWNmZXJlTE8vSHBjWHRLRmEyRHJERzhLLytPL0p3T05VdGk2SWxIaklqR1NYeTNhNTR2elpFS2dqUlZMNDEtLWJyYVlhUDZpMjFkM3NkODYzdlFKWHc9PQ%3D%3D--ae59a2cc849566faae99d47bac27a383db84b8f3',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Referer': 'https://github.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8,lb;q=0.7',
    }

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
