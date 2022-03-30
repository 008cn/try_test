from api_key.api import Api_demo

url = 'https://www.baidu.com'
a = Api_demo()
response = a.do_get(url=url)
response.encoding = 'utf8'
print(response.text)
