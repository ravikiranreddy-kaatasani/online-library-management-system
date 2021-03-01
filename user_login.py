
import pymysql
import base64
import re

mydb=pymysql.connect(host='localhost',user='root',password='root',database='library_mgmt')
cursor=mydb.cursor()

user_mail= input('enter user mail')
password= input('enter passwordd')

def check(mail):
    mail.strip();
    pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    res = re.match(pattern,mail)
    return res

def user_login(user_mail,password):
    try:
        if check(user_mail):
            encoded_pwd = base64.b64encode(password.encode('ascii'))
            if cursor.execute("select user_id,password from user_tt where user_mail_id =%s and password =%s;",(user_mail,encoded_pwd)) == 1:
                print('login')
            else:
                print('invalid credentials')
        else:
            print("Enter valid mail")
    except Exception as e:
        print("Error",e)
        
        
user_login(user_mail,password)
