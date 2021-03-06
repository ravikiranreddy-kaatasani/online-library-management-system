"""[summary]

Returns:
    [type]: [description]
"""
import base64
import smtplib
from random import randint
from email.message import EmailMessage
import pymysql
import valid


mydb=pymysql.connect(host='localhost',user='root',password='root',database='library')
cursor=mydb.cursor()
def otp_generation():
    """[summary]

    Returns:
        [type]: [description]
    """
##  global otp
    otp= [str(randint(1,9)) for i in range(6)]
    otp="".join(otp)
    return otp

def mail_generation(otp,user_mail):
    """[summary]

    Args:
        otp ([type]): [description]
        user_mail ([type]): [description]
    """
    fromaddr = input("Enter  your mail_id to send a request:").strip()
    password = input("Enter your mail password:")
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
def password_match():
    """[summary]

    Returns:
        [type]: [description]
    """
    valid_new_pwd=valid.password_validation(input('enter new password'))
    confirm_password = input('enter confirm password')
    if valid_new_pwd == confirm_password:
        encoded_cn_pwd = base64.b64encode(confirm_password.encode('ascii'))
        # print(encoded_cn_pwd)
        return encoded_cn_pwd
    print('new_password and confirm_password didnot match')
    return password_match()
def forgot_password():
    """[summary]
    """
    print("Select your Choice ")
    user_id = input('enter user id')
    user_id = valid.userid(user_id)
    otp = otp_generation()
    print(otp)
    # mail_generation(otp)
    check_otp = input('enter 6 digit otp sent your mail')
    if check_otp == otp:
        new_pass = password_match()
        cursor.execute('update user set password= %s where user_id = %s',(new_pass,user_id))
        mydb.commit()
        print('password changed')
        mydb.close()
    else:
        print('incorrect OTP')
        forgot_password()
