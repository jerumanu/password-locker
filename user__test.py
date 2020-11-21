import unittest
from user import User , Credential


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

        self.new_credential = Credential("twiter","manjeru",1234567)



    def test__init(self):


        self.assertEqual(self.new_credential.account,"twiter")
        self.assertEqual(self.new_credential.username1,"manjeru")
        self.assertEqual(self.new_credential.password1,1234567)

    def  test_save_credetial(self):
        
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)
    def tearDown(self):
                '''
                tearDown method that does clean up after each test case has run.
                '''
                Credential.credential_list = []
        
    def test_save_multiple_credential(self):
                '''
                test_save_multiple_contact to check if we can save multiple contact
                objects to our contact_list
                '''
                self.new_credential.save_credential()
                test_credential = Credential("Test""whatsapp","manjeru",1234567) # new credetial
                test_credential.save_credential()
                self.assertEqual(len( Credential.credential_list),2)




    def test_delete_credential(self):
                '''
                test_delete_contact to test if we can remove a contact from our contact list
                '''
                self.new_credential.save_credential()
                test_credential = Credential("Test""whatsapp","manjeru",1234567) # new credetial
                test_credential.save_credential()

                self.new_credential.delete_credential()# Deleting a contact object
                self.assertEqual(len(Credential.credential_list),1)
         
if __name__ == '__main__':
    unittest.main()           
