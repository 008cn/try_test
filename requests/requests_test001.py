import requests
from PIL import Image
from io import BytesIO
import json

# 常规调试
# response = requests.get('https://www.baidu.com/')
response = requests.get('https://api.github.com/events')
# print(response)
# response.encoding = 'utf8'
print(response.text)
# print(response.encoding)  # 文本编码
# print(response.content)  # 二进制返回
'''
    各种请求模式
    # response = requests.get('https://api.github.com/events')
    # print(response)
    # r = requests.put('http://httpbin.org/put', data={'key': 'value'})
    # print(r)
    # r = requests.delete('http://httpbin.org/delete')
    # print(r)
    # r = requests.head('http://httpbin.org/get')
    # print(r)
    # r = requests.options('http://httpbin.org/get')
    # print(r)
    # payload = {'key1': 'value1', 'key2': 'value2'}
    # r = requests.get("http://httpbin.org/get", payload)
    # print(r)
    # print(r.url)
    # payload = {'key1': 'value1', 'key2': ['value2', 'value3', '123']}
    # r = requests.get('http://httpbin.org/get', payload)
    # print(r.url)
'''
# r = requests.get('https://api.github.com/events')
# print(r.json())
# print(r.status_code)  # 状态码

# r = requests.get('https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newfanyi-da0cea8f7e.png')
# print(r.text)  # 图片返回乱码
# print(r.content)
'''
    # 不知道
    # i = Image.open(BytesIO(r.content))
    # print(i)
    # print(r.raise_for_status())  
'''
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)

# post请求
# data 参数传入一个元组列表。在表单中多个元素使用同一 key 的时候，这种方式尤其有效：
# payload = (('key1', 'value1'), ('key1', 'value2'))
# r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)
'''
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
# r = requests.post(url, data=json.dumps(payload))
r = requests.post(url, json=payload)
print(r.text)  # 返回的是str字符串
print(r.json()['documentation_url'])  # 获取json某个键的值
print(r.url)
'''
