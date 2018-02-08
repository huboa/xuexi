import requests

r1 = requests.get(
    url='http://dig.chouti.com/',
    headers={
        'Host':'dig.chouti.com',
        'Referer':"http://dig.chouti.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
)
r1_cookie_dict = r1.cookies.get_dict()


r2 = requests.post(
    url='http://dig.chouti.com/login',
    data={
        'phone':'8613121758648',
        'password':'woshiniba',
        'oneMonth':1,
    },
    headers={
        'Host':'dig.chouti.com',
        'Referer':"http://dig.chouti.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    },
    cookies=r1_cookie_dict
)

r3 = requests.post(
    url='http://dig.chouti.com/link/vote?linksId=17035631',
    headers={
        'Host':'dig.chouti.com',
        'Referer':"http://dig.chouti.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    },
    cookies=r1_cookie_dict
)

print(r3.text)