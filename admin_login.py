"""
Admin _module

This a custom module that validates the admin
"""
import base64
import valid
from connection import cursor


def admin_login():
    """This is a function that validates the .
    Args:
        admin_mail (string): Admin email address
        password (string): Admin Password
        cursor (DB_class): cursor class
        mydb (DB_class): connection class
    Returns:
        string : returns the user id of the validated admin
    """
    try:
        admin_mail =valid.email_validation(input('enter admin mail '))
        password = input("Enter you password")
        encoded_pwd = base64.b64encode(password.encode('ascii'))
        query = "select user_id from user \
            where mail_id =%s and password =%s and is_admin_flag = %s;"
        if cursor.execute(query,(admin_mail, encoded_pwd, '1')):
            print('admin login')
            admin_uid = cursor.fetchone()
            return admin_uid[0]
        print('invalid credentials')
    except Exception as exception_e:
        print('Error',exception_e)
