"""Main Module to run userSignup, userlogin, forgotpassword
"""

from user_login import user_login
from user_signup import user_signup
from forgot_password import forgot_password


def start():
    """ function to run userSignup, userlogin, forgotpassword
    """
    while True:
        try:
            welcome_screen="\n \
            ---HI WELCOME TO OJAS ONLINE LIBRARY MANAGEMENT SYSTEM---\
                \n\n  1.User Login \n  2.User Signup \n  3.Forgot Password \n  Enter your choice : "
            user_input = str(input(welcome_screen)).lower()
            if user_input in ('1', 'login'):
                user_id =  user_login()
                if user_id:
                    print( user_id )
            elif user_input in ('2', 'signup'):
                user_signup()
            elif user_input in ('3', 'Forgot password'):
                forgot_password()
            else:
                print("Wrong input")
        except Exception as exception_e:

            print("Error", exception_e)

start()
