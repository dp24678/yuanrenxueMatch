import random
import time
import pywasm
import requests


def m():
    """
    t1 = parseInt(Date.parse(new Date())/1000/2);
    t2 = parseInt(Date.parse(new Date())/1000/2 - Math.floor(Math.random() * (50) + 1));
    return window.q(t1, t2).toString() + '|' + t1 + '|' + t2;
    :return:
    """
    t1 = int(time.time() / 2)
    t2 = int(time.time() / 2 - int(random.uniform(1, 51)))
    vm = pywasm.load('./a.wasm')
    r = vm.exec('encode', [t1, t2])
    return f"{r}|{t1}|{t2}"

import requests

cookies = {
    # 'tk': '-1309588185006210753',
    'sessionid': '50pq3l1p9e4fgxtqxzkst5a8jkike0hv',
}

headers = {
    'authority': 'match.yuanrenxue.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1672884000; tk=-1309588185006210753; sessionid=50pq3l1p9e4fgxtqxzkst5a8jkike0hv; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1672887649; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1672887649; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1672887649',
    'pragma': 'no-cache',
    'referer': 'https://match.yuanrenxue.com/match/15',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

response = requests.get('https://match.yuanrenxue.com/static/match/match15/main.wasm', cookies=cookies, headers=headers)
with open("a.wasm", "wb") as f:
    f.write(response.content)


headers = {
    'authority': 'match.yuanrenxue.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1672884000; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1672884000',
    'pragma': 'no-cache',
    'referer': 'https://match.yuanrenxue.com/match/15',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'yuanrenxue.project',
    'x-requested-with': 'XMLHttpRequest',
}

s = requests.Session()
prices = []
for i in range(1, 6):
    params = {
        'm': m(),
        'page': str(i),
    }
    response = requests.get('https://match.yuanrenxue.com/api/match/15', params=params, cookies=cookies,
                            headers=headers)
    print(response.text)
    prices.extend([i['value'] for i in response.json()['data']])

print(prices)
print(len(prices))
print(sum(prices))