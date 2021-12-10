import requests
from lxml import etree
#从响应中获取我们想要的数据
url='https://movie.douban.com/top250'
headers={
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Mobile Safari/537.36'
}
text= requests.get(url, headers=headers).text

# 用 xpath提取数据要点
dom = etree.HTML(text)
# print(dom)
# ret=dom.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/p[1]/text()')[1].strip()
ret=dom.xpath('//div[@class="hd"]/a/span[@class="title"]/text()')#xpath语句
for i in ret:
    print(i.strip())