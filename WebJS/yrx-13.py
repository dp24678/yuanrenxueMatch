import re
import requests
from requests.utils import add_dict_to_cookiejar

headers = {
    'authority': 'match.yuanrenxue.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://match.yuanrenxue.com/match/13',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'yuanrenxue.project',
}
s = requests.Session()
add_dict_to_cookiejar(s.cookies, {'sessionid': 'c99w039nha0v1hq3phnldbl26zv76fnn'})
response = s.get('https://match.yuanrenxue.com/match/13', headers=headers)
cookieStr = re.search(r"\.cookie=(.*?);path=/", response.text).group(1)
cookieStr = re.sub(r"[\(\)'\+]", "", cookieStr)
key = cookieStr.split('=')[0]
value = cookieStr.split('=')[1]
add_dict_to_cookiejar(s.cookies, {key: value})
print(s.cookies)
prices = []
for i in range(1, 6):
    params = {
        'page': str(i),
    }
    response = s.get('https://match.yuanrenxue.com/api/match/13', params=params, headers=headers)
    print(response.text)
    print(s.cookies.items())
    prices.extend([i['value'] for i in response.json()['data']])

print(prices)
print(len(prices))
print(sum(prices))
