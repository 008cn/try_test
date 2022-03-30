import requests

'''
    封装接口,关键字驱动
'''


class Api_demo:
    def do_post(self, url, josn=None, header=None, **kwargs):
        return requests.post(url=url, josn=josn, header=header, **kwargs)

    # 教程有误
    # def do_get(self, url, params=None, header=None, **kwargs):
    #     return requests.get(url=url, params=params, header=header, **kwargs)

    def do_get(self, url, params=None, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

