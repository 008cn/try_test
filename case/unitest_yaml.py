import requests
import ddt
import unittest


class Test_case(unittest.TestCase):
    def test_get_00(self):
        url = 'https://api.github.com/some/endpoint'
        response = requests.get(url=url)
        # print(response.json())
        self.assertCountEqual('Not Found', response.json()['message'])

    def test_get_01(self):
        url = 'https://api.github.com/some/endpoint'
        response = requests.get(url=url)
        # print(response.json())
        self.assertCountEqual('https://docs.github.com/rest', response.json()['documentation_url'])


if __name__ == '__main__':
    unittest.main
