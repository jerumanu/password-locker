#!/usr/bin/env python3.6
from user import User,Credential

def create_user(username,password):
    '''
    creating new user
    '''
    new_user = User(username,password)

    return new_user



def  save_user(user):
    '''
    save  user
    '''
    user.save_user()


