"""
关键点：JS混淆加密
js hook cookie的设置点
hook代码：
(function () {
    'use strict';
    Object.defineProperty(document, 'cookie', {
        set: function (cookie) {
            console.log('Setting cookie', cookie);
            // RM4hZBv0dDon443M 为要断点的cookie key
            if (cookie.indexOf('RM4hZBv0dDon443M') != -1) {
                debugger;
            }
            return cookie;
        }
    });
})();

hook window._$ss 生成位置，注意 此hook代码如果在油猴使用 需要设置油猴 // @run-at    document-start（在页面加载前注入脚本）否则断不住
(function () {
    Object.defineProperty(window, '_$ss', {
        set: function(val){
            console.log('_$ss：'+ val);
            debugger;
        }
    })
})();


(function() {
    'use strict';
    var value_;
    Object.defineProperty(window, '$_zw', { // 修改_$ss为你需要查询的window属性
        get: function() {
            console.log('Window Hook捕获到->', value_);
            debugger;
            return value_;
        },
        set: function(value) {
            value_ = value;
            console.log('Window Hook捕获到->', value_);
            debugger;
            return value;
        },
    });
})();


new_0x474032 = _0x474032;
_0x474032 = function (){
    result = new_0x474032(arguments)
    console.log("时间戳：" + arguments[0] + "  加密后：" + result)
    return result
}
"""
import json
import execjs
import requests
with open(r"yrx-05.js", 'r', encoding="utf8") as f:
    js_str = f.read()

js_ = execjs.compile(js_str)

params_m, params_f, cookie_m, cookie_RM4hZBv0dDon443M = js_.call("getArgs")
print(params_m, params_f, cookie_m, cookie_RM4hZBv0dDon443M)

cookies = {
    'sessionid': 'x01t391cix58aoriajd3tbvx5fhi24vl',
    # 'm': cookie_m,  这里不传递 m参数一样能拿到数据
    'RM4hZBv0dDon443M': cookie_RM4hZBv0dDon443M,
}


headers = {
    'authority': 'match.yuanrenxue.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://match.yuanrenxue.com/match/5',
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
    print(f"第{i}页")
    params = {
        'page': str(i),
        'm': params_m,
        'f': params_f,
    }
    response = s.get('https://match.yuanrenxue.com/api/match/5', params=params, headers=headers, cookies=cookies)
    print(response.text)
    prices.extend([i['value'] for i in json.loads(response.text)['data']])

print(prices)
print(len(prices))
prices.sort(reverse=True)
print(sum(prices[:5]))