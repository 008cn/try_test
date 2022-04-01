from ddt import ddt, file_data
import unittest


@ddt
class Test(unittest.TestCase):

    @file_data("../data/data.yaml")
    def test01(self, data):
        print(data)


if __name__ == '__main__':
    unittest.main
