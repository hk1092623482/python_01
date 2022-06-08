


from project02_gai.iter03_add_user import login
from loguru import logger

# login_result = login('admin','123456')
# logger.debug("登录返回数据:{}".format(login_result))

import unittest
import sys

class Testlogin(unittest.TestCase):

    # 初始化类方法
    @classmethod
    def setUpClass(cls) -> None:
        print("开始运行方法:", sys._getframe().f_code.co_name)
    # 清空类方法
    @classmethod
    def tearDownClass(cls) -> None:
        print("开始运行方法:", sys._getframe().f_code.co_name)


    # 初始化方法
    def setUp(self) -> None:
        print("开始运行方法:",sys._getframe().f_code.co_name)
    # 清除方法
    def tearDown(self) -> None:
        print("开始运行方法:", sys._getframe().f_code.co_name)

    # case1 : 输入正确的用户和正确的密码进行登录
    def test_login_success(self):
        print("开始运行方法:", sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login('admin','123456').get('code')
        self.assertEqual(except_value,actual_value)

    # case2 : 输入错误的用户名或密码登录
    def test_user_wrong(self):
        print("开始运行方法:", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login('bcd', '123456').get('code')
        self.assertEqual(except_value, actual_value)
    # case3 : 输入空的用户或密码登录
    def test_password_is_null(self):
        print("开始运行方法:", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login('admin', '').get('code')
        self.assertEqual(except_value, actual_value)

if __name__ == '__main__':
    # 创建一个套件a
    suite_a = unittest.TestLoader().discover('.',pattern='test_login_testdiscover1.py')

    print(suite_a)

    runner = unittest.TextTestRunner()
    runner.run(suite_a)