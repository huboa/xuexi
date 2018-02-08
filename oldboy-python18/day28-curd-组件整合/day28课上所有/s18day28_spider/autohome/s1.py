# 伪造浏览器发送Http请求
import requests
from bs4 import BeautifulSoup

# 下载页面
response = requests.get(url='https://www.autohome.com.cn/news/')
response.encoding = 'gbk'
print(response.status_code)
# response.content
# response.text

# 正则匹配
# 别人帮你写正则
# 将下载的页面进行结构化处理
# HTML结构树
soup = BeautifulSoup(response.text,"html.parser")

# 找到匹配成功的第一个标签：标签对象
div = soup.find(name='div',id='auto-channel-lazyload-article')
# 找到多个标签[标签对象，标签对象，]
li_list = div.find_all(name='li')
for li in li_list:
    h3 = li.find(name='h3')
    p = li.find(name='p')
    a = li.find(name='a')
    img = li.find(name='img')
    if not h3:
        continue
    print(h3.text)
    print(p.text)
    # print(a.attrs['href'])
    print(a.get('href'))
    img_url = "https:" + img.get('src')

    img_response = requests.get(img_url)
    file_name = img_url.rsplit('/',maxsplit=1)[1]
    with open(file_name,'wb') as f:
        f.write(img_response.content)
    print('-----------------------------')






