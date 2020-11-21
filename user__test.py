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



    def test__init(self):


        self.assertEqual(self.new_credetial.account,"twiter")
        self.assertEqual(self.new_credetial.username1,"manjeru")
        self.assertEqual(self.new_credetial.password1,1234567)

    def  test_save_credetial(self):
        
        self.new_credetial.save_credetial()
        self.assertEqual(len(Credetial.credential_list),1)
if __name__ == '__main__':
    unittest.main()           
