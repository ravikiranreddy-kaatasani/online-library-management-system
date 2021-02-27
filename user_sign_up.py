import pymysql
import base64
from re import fullmatch

mydb=pymysql.connect(host='localhost',user='root',password='root',database='library_management_trial')
cursor=mydb.cursor()

user_name=input('enter user name').strip()
user_mail= input('enter user mail').strip()
password= input('enter passwordd').strip()

def user_signup(user_name,user_mail,password):
    if cursor.execute("select user_mail_id from user_tt where user_mail_id =%s;",(user_mail)) == 1:
        print('user already exists')
    else:

        if fullmatch("(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}",pswd):
            encoded_pwd = base64.b64encode(password.encode('ascii'))
            cursor.execute("insert into user_tt (user_name,user_mail_id,password) values(%s,%s,%s)",(user_name,user_mail,encoded_pwd))
            mydb.commit()
        else:
            print("--Password did not match the requirements--")
user_signup(user_name,user_mail,password)
