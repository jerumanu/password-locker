import unittest
from user import User , Credetial


class UserTest(unittest.TestCase):

    def setUp(self):

        self.new__user = User("jerumanu",91547712)

    def test__init(self):

        self.assertEqual(self.new__user.username,"jerumanu")
        self.assertEqual(self.new__user.password,91547712)
    def  test_save_user(self): 
        self.new__user.save_user()
        self.assertEqual(len(User.user__list),1)





class CredetialTest(unittest.TestCase):
    def setUp(self):

        self.new_credetial = Credetial("twiter","manjeru",1234567)
    def    

if __name__ == '__main__':
    unittest.main()           
