from urllib.parse import urlparse
import requests

url = 'https://www.gamer.com.tw/'

# urlparse() 用於網址解析
URLparse = urlparse(url)

print("scheme:%s" % URLparse.scheme)
print("netloc:%s" % URLparse.netloc)
print("port:%s" % URLparse.port)
print("path:%s" % URLparse.path)
print("query:%s" % URLparse.query)
print('-------------------------')
#類似html 中的GET
request = requests.get(url)
request.encoding = 'UTF-8'
relist = request.text.splitlines()
for i in relist:
    if '巴哈' in i:
        print(i)
