from collections import Counter
import requests

cookies = {
    'sessionid': 't',
}
headers = {'content-length': '0',
           'pragma': 'no-cache',
           'cache-control': 'no-cache',
           'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
           'sec-ch-ua-mobile': '?0',
           'user-agent': 'yuanrenxue.project',
           'sec-ch-ua-platform': '"Windows"',
           'accept': '*/*',
           'origin': 'https://match.yuanrenxue.com',
           'sec-fetch-site': 'same-origin',
           'sec-fetch-mode': 'cors',
           'sec-fetch-dest': 'empty',
           'referer': 'https://match.yuanrenxue.com/match/3',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'zh-CN,zh;q=0.9'}
s = requests.Session()
# 实现header 请求头参数顺序不变，requests默认会打乱headers的参数顺序
s.headers.clear()
s.headers.update(headers)


prices = []
for i in range(1, 6):
    response = s.post('https://match.yuanrenxue.com/jssm', verify=False, cookies=cookies)
    print(response.headers)
    print(response.cookies)
    print(response.status_code)

    params = {
        'page': str(i),
    }
    response = s.get('https://match.yuanrenxue.com/api/match/3', params=params)
    print(response.text)
    prices.extend([i['value'] for i in response.json()['data']])

print(prices)
print(len(prices))
counter = Counter(prices)
most_counterNumber = counter.most_common(1)[0][0]
print(most_counterNumber)
