"""Admin Login Main Module

"""
import admin_login
import forgot_password
from connection import mydb

while True:
    try:
        welcome_screen = "Admin Dashboard \n 1.Login \n 2.Forgot Password \n  Enter your Choice : "
        user_input = input(welcome_screen).lower()
        if user_input in ('1', 'login'):
            user_id =  admin_login.admin_login()
            if user_id:
                print(user_id)
        elif user_input in ('2', 'forgot','password','forgot password'):
            forgot_password.forgot_password()
        else:
            print("Wrong input")
    except Exception as exception_e:
        print('Error', exception_e)
    
        
