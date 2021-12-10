import json
import requests
url="https://rms.shop.jd.com/json/pop/shopInfo.action?callback=jQuery7670726&ids=10549064%2C10556303%2C1000000158%2C1000087624&_=1638086577066"
#text=requests.get(url).text
headers={
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94\
.0.4606.81 Mobile Safari/537.36'
}
text=requests.get(url, headers=headers).content.decode('gbk')
text=text.replace("jQuery7670726(", "").replace(")", "")
print(text)
for item in text:
    print(item)
    data=json.loads(item)
    print(data)
#json.loads十是把字符串格式转成字典格式