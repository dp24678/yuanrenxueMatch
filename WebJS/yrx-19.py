"""
关键点：TLS指纹识别  
https://mp.weixin.qq.com/s/Qx7PjnBgrTR30oCurU6CGw
https://blog.csdn.net/god_zzZ/article/details/123010576
https://blog.csdn.net/cqcre/article/details/128025953
https://mp.weixin.qq.com/s/og2IKo8lcydh8PROUPD7jQ
https://segmentfault.com/a/1190000041699815
https://blog.csdn.net/qq_42519299/art
https://blog.csdn.net/qq_42519299/article/details/129733253
https://www.cnblogs.com/ospider/p/python-curl-cffi-tls-fingerprint.html
https://yifei.me/note/2719
https://jishuin.proginn.com/p/763bfbd73fc3
"""

# 方法一、使用了大佬 https://github.com/zero3301/pyhttpx 的库，还支持http2.0 奈斯啊
import json
import pyhttpx


cookies = {
    'sessionid': 'jmr860ywwaiw7rvhbnk928clcsbto010'
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

# 方法二、使用 curl_cffi库

# from curl_cffi import requests
#
#
# cookies = {
#     'sessionid': 'jmr860ywwaiw7rvhbnk928clcsbto010'
# }
#
# headers = {
#     'authority': 'match.yuanrenxue.com',
#     'accept': 'application/json, text/javascript, */*; q=0.01',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'cache-control': 'no-cache',
#     'pragma': 'no-cache',
#     'referer': 'https://match.yuanrenxue.com/match/19',
#     'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'yuanrenxue.project',
#     'x-requested-with': 'XMLHttpRequest',
# }
#
# prices = []
# for i in range(1, 6):
#     params = {
#         'page': str(i),
#     }
#     response = requests.get('https://match.yuanrenxue.com/api/match/19', params=params, headers=headers, cookies=cookies,  allow_redirects=False, impersonate="chrome110")
#     print(response.text)
#     prices.extend([i['value'] for i in json.loads(response.text)['data']])
#
# print(prices)
# print(len(prices))
# print(sum(prices))


# 方法三, 此题场景不适合 但是其他验证jar3的测试可用


# 后测试可用 但需要将

# from requests.adapters import HTTPAdapter
# from urllib3.util.ssl_ import create_urllib3_context
# import random
# import requests
# import json
#
# # ORIGIN_CIPHERS = ('ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
# #                   'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES')
#
# # 此题似乎测试 只要jar3 长度差不多 就可以通过
# ORIGIN_CIPHERS = 'ECDH+AESGCM:DH+AESGCM:ECDH+AES256:RSA+3DES'
#
#
# class DESAdapter(HTTPAdapter):
#     def __init__(self, *args, **kwargs):
#         """
#         在请求中重新启用 3DES 支持的传输适配器
#         A TransportAdapter that re-enables 3DES support in Requests.
#         """
#         CIPHERS = ORIGIN_CIPHERS.split(':')
#         random.shuffle(CIPHERS)
#         CIPHERS = ':'.join(CIPHERS)
#         self.CIPHERS = CIPHERS + ':!aNULL:!eNULL:!MD5'
#         super().__init__(*args, **kwargs)
#
#     def init_poolmanager(self, *args, **kwargs):
#         context = create_urllib3_context(ciphers=self.CIPHERS)
#         kwargs['ssl_context'] = context
#         return super(DESAdapter, self).init_poolmanager(*args, **kwargs)
#
#     def proxy_manager_for(self, *args, **kwargs):
#         context = create_urllib3_context(ciphers=self.CIPHERS)
#         kwargs['ssl_context'] = context
#         return super(DESAdapter, self).proxy_manager_for(*args, **kwargs)
#
# cookies = {
#     'sessionid': 'jmr860ywwaiw7rvhbnk928clcsbto010'
# }
# headers = {
#     'authority': 'match.yuanrenxue.com',
#     'accept': 'application/json, text/javascript, */*; q=0.01',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'cache-control': 'no-cache',
#     'pragma': 'no-cache',
#     'referer': 'https://match.yuanrenxue.com/match/19',
#     'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'yuanrenxue.project',
#     'x-requested-with': 'XMLHttpRequest',
# }
# s = requests.Session()
# s.headers.update(headers)
#
#
# prices = []
# for i in range(1, 6):
#     params = {
#         'page': str(i),
#     }
#     s.mount('https://match.yuanrenxue.com', DESAdapter())
#     response = s.get('https://match.yuanrenxue.com/api/match/19', params=params, headers=headers, cookies=cookies)
#     print(response.text)
#     prices.extend([i['value'] for i in json.loads(response.text)['data']])
#
# print(prices)
# print(len(prices))
# print(sum(prices))