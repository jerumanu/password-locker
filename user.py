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



class Credetial:

    credential_list = []

    def __init__(self,account,username1,password1):



        self.account = account
        self.username1 = username1
        self.password1 = password1


