"""This module contains OTP generation,mail_generation,password_match,forgot_password functions

"""
import base64
import smtplib
from random import randint
from email.message import EmailMessage
import valid
from connection import cursor , mydb

def otp_generation():
    """This function generates OTP
    Returns:
        string: One  Time Password
    """
    otp= [str(randint(1,9)) for i in range(6)]
    otp="".join(otp)
    return otp

def mail_generation(otp,user_mail):
    """This function is a custom module to send mail
    Args:
        otp (string): One  Time Password
        user_mail (string): User Email Address
    """
    try:
        fromaddr = "ojas.python@gmail.com"
        password = "Ojas@1525"
        message= otp
        msg = EmailMessage()
        msg["Subject"] = "OTP"
        msg["From"] = fromaddr
        msg["To"] = user_mail
        msg.set_content(message)
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(fromaddr,password)
        server.send_message(msg)
        server.quit()
        print("OTP IS SENT TO YOUR MAIL ADDRESS")
    except Exception as exception_e:
        print("Error",exception_e)
def password_match():
    """This function validates and returns encrypted password

    Returns:
        string: Returns encrypted password
    """
    valid_new_pwd=valid.password_validation(input('enter new password : '))
    confirm_password = input('enter confirm password : ')
    if valid_new_pwd == confirm_password:
        encoded_pwd = base64.b64encode(confirm_password.encode('ascii'))
        # print(encoded_cn_pwd)
        return encoded_pwd
    print('new_password and confirm_password did not match \n ')
    return password_match()

def forgot_password():
    """This function updates the new encrypted password to the db
    """
    user_mail = valid.email_validation(input('enter user mail : ').strip().lower())
    query= "select mail_id from user where mail_id =%s;"
    if cursor.execute(query,(user_mail)) :
        otp = otp_generation()
        print(otp)
        mail_generation(otp,user_mail)
        check_otp = input('enter 6 digit otp sent your mail : ')
        if check_otp == otp:
            new_pass = password_match()
            cursor.execute('update user set password= %s where mail_id = %s',(new_pass,user_mail))
            mydb.commit()
            print('password changed')
        else:
            print('incorrect OTP \n')
            forgot_password()
    else:
        print("User Not Found")
    
