#!/usr/bin/env python3.6
from user import User,Credential

def create_user(username,password):
    '''
    creating new user
    '''
    new_user = User(username,password)

    return new_user


# def sign_in(username, password):
#     user_exists = User.user_exist(username,password)
#     return user_exists


def  save_user(user):
    
    user.save_user()


# def delete user(user):

#     user.delete _user()





# credential


def create_credential (account,username1,password1):
    new_credential = Credential(account,username1,password1)
    return new_credential 


def save_credential(credential):
    credential.save_credential()


def delete_credential(Credential):


  Credential.delete_credential()

def find_credential(account):


    return  Credential.find_by_account(account)

def display_credential():
    '''
    Function that returns all the saved contacts
    '''
    return Credential.display_credential()

def check_existing_credential(account):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Credential.credential_exist(account)

def main():
    print("Hi! welcome to an application that help you manage your credentials")
    print('Welcome to Password Locker. Use the these commands to proceed: CA = create account,' )
    short_code = input().lower()   
    if short_code == 'ca':
        print('Enter new account details')
        print('*' * 100)
        username = input('Enter Username: ')
        while True:
            print('use :  MP = to manually enter your own password')
            password_choice = input().lower()
            if password_choice == 'mp':
                password = input('Enter Password: ')
                break
          
            else:
                print('Invalid short code. Please try again')
                
            save_user(create_user(username, password))
        print('*' * 100)
        print(f'Welcome {username} to your new account your password is <--- {password} --->')
        print('*' * 100)
    
         
    while True:
        print('Use these short codes to manage credentials: \n NC = new credential, \n VC = display credentials,\n SC =     find credential  \n Dc = delete credential, \n  EX = exit application')
        short_code = input().lower()
        if short_code == 'nc':
            print('Enter New Credential Details')
            print('*' * 100)
            account = input('Account Name : ')
            username1 = input('Username : ')
            while True:
                print('Use: MP = manually enter password?')
                password_choice = input().lower()
                if password_choice == 'mp':
                    password = input('Enter password : ')
                    break
                
                else:
                    print('Invalid short code. Please try again')
                print('*' * 100)
            save_credential(create_credential(account, username1, password))
            print('*' * 100)
            print(f'Your {account} account has been saved')
            print('*' * 100)
        elif short_code == 'vc':
            
            if display_credential():
                print('Your saved credentials are:')
                for account in display_credential():
                    print('-' * 100)
                    print(f'   Username: {username1} \n Password: {password}')
                    print('-' * 100)
            else:
                print('*' * 100)
                print('You have No Credentials. Please Create One')
                print('*' * 100)
                
        elif short_code == 'dc':
            print('Enter Account name to delete...')
            name = input('Acount Name : ')
            print('*' * 100)
            if find_credential(name):
                name_result = find_credential(name)
                name_result.delete_credential()
                print(f'Account {name} has been successfully deleted ')
                print('*' * 100)
                
            else:
                print('Incorrect account name')
                print('*' * 100)
                
        elif short_code == 'sc':
            print('Enter Account Name To Search...')
            search = input('Account Name : ')
            print('*' * 100)
            if find_credential(search):
                search = find_credential(search)
                print(f'Account Name: {search} ')
                print('*' * 100)
            else:
                print('Credential does not exist')
                print('*' * 100)
            
        
            
        elif short_code == 'ex':
            print('Goodbye')
            print('*' * 100)
            break
            
        else:
            print('Invalid Short code. Please try again!')
            print('*' * 100)
    
   
                        
if __name__ == '__main__':
    main()
    