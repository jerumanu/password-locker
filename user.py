class  User:

    user__list = []
    
    def __init__ (self,username,password):
        
        
        
        self.username = username
        self.password = password

 
    def save_user(self):

        '''
    user method saves contact objects into contact_list
        '''

        User.user__list.append(self)



class Credential:

    credential_list = []

    def __init__(self,account,username1,password1):



        self.account = account
        self.username1 = username1
        self.password1 = password1

     
    def save_credential(self):

        '''
        user method saves contact objects into contact_list
        '''

        Credential.credential_list.append(self)




    def delete_credential(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Credential.credential_list.remove(self)         




    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
        number: Phone number to search for
        Returns :
        Contact of person that matches the number.
        '''

        for credential in cls.credential_list:
            if credential.account == account:
                 print(credential)
                 return credential