import time
import execjs
import requests

""" 
关键点：webpack 爬虫 使用了自执行函数，此题补环境时有坑 try内缺失的参数不会通过报错提示看到

https://baijiahao.baidu.com/s?id=1714221906158503382&wfr=spider&for=pc
"""

with open(r"yrx-16.js", 'r', encoding="utf8") as f:
    js_str = f.read()


def getM():
    t = str(int(time.time() * 1000))
    print(t)
    #
    # with open(r"yrx-.py", 'w', encoding="utf8") as f:
    #     f.write(f'"""{js_str}"""')
    js_ = execjs.compile(js_str)
    res = js_.call("btoa_", t)
    print(res)
    return res, t


cookies = {
    'sessionid': 'zvf5p2k52ufq09il06b1uc100dmpqwxs',
}
headers = {
    'authority': 'match.yuanrenxue.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1672884000; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1672884000',
    'pragma': 'no-cache',
    'referer': 'https://match.yuanrenxue.com/match/16',
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
    m, t = getM()
    params = {
        'page': i,
        'm': m,
        't': t,
    }
    response = s.get('https://match.yuanrenxue.com/api/match/16', params=params, cookies=cookies, headers=headers)
    print(response.text)
    prices.extend([i['value'] for i in response.json()['data']])

print(prices)
print(len(prices))
print(sum(prices))