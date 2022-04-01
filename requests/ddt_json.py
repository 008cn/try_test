from ddt import ddt, file_data
import unittest


@ddt
class Test(unittest.TestCase):

    @file_data("../data/data.json")
    def test01(self, username, password):
        print(username, password)


if __name__ == '__main__':
    unittest.main()
