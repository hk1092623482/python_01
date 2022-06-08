from project02_gai.iter03_add_user import login

from parameterized import parameterized
import unittest


lst_data = [(0,'admin','123456'),(0,'dev','123456'),(1,'dev','1234567')]

class Testlogin(unittest.TestCase):


    @parameterized.expand(lst_data)
    def test_login(self,except_value,username,password):

        actual_value = login(username,password).get('code')
        self.assertEqual(except_value,actual_value)


if __name__ == '__main__':
    unittest.main()
