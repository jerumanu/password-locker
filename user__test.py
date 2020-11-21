import unittest
from user import User

class UserTest(unittest.TestCase):

    def setUp(self):

        self.new__user = User("jerumanu",91547712)

    def test__init(self):

        self.assertEqual(self.new__user.username,"jerumanu")
        self.assertEqual(self.new__user.password,91547712)
    
    def  test-save_user(self): 


if __name__ == '__main__':
    unittest.main()           
