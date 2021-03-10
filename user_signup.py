"""This module is creates the user and updates in the database.
"""
import base64
import valid
from connection import cursor , mydb
from forgot_password import otp_generation,mail_generation,password_match
def user_signup():
    """This module is used for user Signup
    """
    try:
        # Signup User Input
        user_id = valid.userid(input('enter user id : ').strip().lower())
        query = "select mail_id from user where user_id =%s;"
        if cursor.execute(query, (user_id)):
            print('user id already exists')
            user_signup()
        else:
            user_name = valid.user_name_validation(input('enter user name : ').strip())
            user_mail = valid.email_validation(input('enter user mail : ').strip().lower())
            query = "select mail_id from user where mail_id =%s;"
            if cursor.execute(query, (user_mail)):
                print('mail_id already exists')
                user_signup()    
            else:
                otp = otp_generation()
                print(otp)
                mail_generation(otp,user_mail)
                def otp_check():
                    check_otp = input('enter 6 digit otp sent your mail : ')
                    if check_otp == otp:
                        encoded_pwd = password_match()
                        query = "insert into user (user_id,user_name,mail_id,password) values(%s,%s,%s,%s)"
                        cursor.execute(query,(user_id,user_name, user_mail, encoded_pwd))
                        mydb.commit()
                        print("User Creation Successful")
                    else:
                        print('incorrect OTP \n')
                        otp_check()

                otp_check()
    except Exception as exception_e:
        print("Error",exception_e)

