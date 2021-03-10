"""This custom module returns user id of the validated user

    Returns:
        string : returns the user id of the validated user
"""
import base64
from connection import cursor
def user_login():
    """This custom module returns user id of the validate user
    Returns:
        string: returns the user id of the validated user
    """
    try:
        user_mail= input('enter user mail : ')
        password= input('enter password : ')
        if user_mail and password :
            encoded_pwd = base64.b64encode(password.encode('ascii'))
            query= "select user_id from user where mail_id =%s and password =%s;"
            if cursor.execute(query,(user_mail,encoded_pwd)):
                user_id = cursor.fetchone()
                print('login')
                return  user_id[0]
        else:
            print('Invalid Credentials \n\n--Login Again--\n  ')
    except Exception as exception_e:
        print("Error", exception_e)
    