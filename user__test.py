import unittest
from user import User, Credential


class UserTest(unittest.TestCase):

    def setUp(self):

        self.new__user = User("jerumanu",91547712)

    def test__init(self):

        self.assertEqual(self.new__user.username,"jerumanu")
        self.assertEqual(self.new__user.password,91547712)
    def  test_save_user(self): 
        self.new__user.save_user()
        self.assertEqual(len(User.user__list),1)

        
    @classmethod
    def user_exist(cls, username,password):
        current_user = ''
        for user in User.user__list:
           if(user.username == username and user.password == password):
                current_user = user.username
        return current_user

 

class CredentialTest(unittest.TestCase):
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

    def test_find_credentials(self):
        self.new_credential.save_credential()
        test_credential = Credential("whatsapp", "manjeru", 12345)
        test_credential.save_credential()

        found_credential = Credential.find_by_account('whatsapp')
        found_credential = found_credential
        self.assertEqual(found_credential,test_credential)
        


    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("whatsapp", "manjeru", 12345) # new contact
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("whatsapp")

        self.assertTrue(credential_exists)



    def test_display_all_credential(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(Credential.display_credential(),Credential.credential_list)
    # def test_find_credential_by_account(self):
    #            '''
    #            test to check if we can find a contact by phone number and display information
    #            '''

    #            self.new_credential.save_credential()
    #            test_credential = Credential("Test""whatsapp","manjeru",1234567) # new credetial
    #            test_credential.save_credential()

    #            found_credential = Credential.find_by_account('whatsapp')
    #            self.assertEqual(found_credential.account,test_credential.account)


         
if __name__ == '__main__':
    unittest.main()           
