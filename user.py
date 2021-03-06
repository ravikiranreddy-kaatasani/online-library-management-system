"""[summary]
"""

import user_login
import user_signup
import forgot_pass

while True:
    try:
        STRING="HI WELCOME TO OJAS ONLINE LIBRARY MANAGEMENT SYSTEM \n  1.User Login \n  2.User Signup \n  3.Forgot Password \n    Enter your choice : "
        USER_INPUT = str(input(STRING)).lower()
        if USER_INPUT in ('1', 'login'):
            user_login.start()
        elif USER_INPUT in ('2', 'signup'):
            user_signup.start()
        elif USER_INPUT in ('3', 'Forgot password'):
            forgot_pass.forgot_password()
        else:
            print("Wrong input")
    except Exception as exception_e:
        print("Error", exception_e)
