import base64
import requests




headers = {
    'authority': 'match.yuanrenxue.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://match.yuanrenxue.com/match/12',
    # 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'yuanrenxue.project',
    'x-requested-with': 'XMLHttpRequest',
}



cookies = {"sessionid": "erronahd6645etldc6x937vu28jtg08n"}
prices = []
for i in range(1, 6):
    name = f'yuanrenxue{i}'
    # 编码
    m = base64.b64encode(name.encode()).decode()
    print(m)
    params = {
        'page': str(i),
        'm': m,
    }
    response = requests.get('https://match.yuanrenxue.com/api/match/12', params=params, headers=headers, cookies=cookies)
    print(response.text)
    prices.extend([i['value'] for i in response.json()['data']])

print(prices)
print(len(prices))
print(sum(prices))