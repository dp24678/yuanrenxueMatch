import time
import execjs
import requests

""" 
关键点：TLS指纹识别  
https://mp.weixin.qq.com/s/Qx7PjnBgrTR30oCurU6CGw
https://blog.csdn.net/god_zzZ/article/details/123010576
https://blog.csdn.net/cqcre/article/details/128025953
https://mp.weixin.qq.com/s/og2IKo8lcydh8PROUPD7jQ
https://segmentfault.com/a/1190000041699815
最终使用了大佬 https://github.com/zero3301/pyhttpx 的库，还支持http2.0 奈斯啊
"""
import json
import pyhttpx


cookies = {
    'sessionid': 'dl8n663groarn8tjgyy14cs5ovb92xa2'
}
headers = {
    'authority': 'match.yuanrenxue.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://match.yuanrenxue.com/match/19',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'yuanrenxue.project',
    'x-requested-with': 'XMLHttpRequest',
}
sess = pyhttpx.HttpSession(browser_type='chrome')
prices = []
for i in range(1, 6):
    params = {
        'page': str(i),
    }
    response = sess.get('https://match.yuanrenxue.com/api/match/19', params=params, headers=headers, cookies=cookies)
    print(response.text)
    prices.extend([i['value'] for i in json.loads(response.text)['data']])

print(prices)
print(len(prices))
print(sum(prices))