import pymysql
import base64

mydb=pymysql.connect(host='localhost',user='root',password='root',database='library_management_trial')
cursor=mydb.cursor()

user_mail= input('enter user mail')
password= input('enter passwordd')


def user_login(user_mail,password):
    encoded_pwd = base64.b64encode(password.encode('ascii'))
    if cursor.execute("select user_id,password from user_tt where user_mail_id =%s and password =%s;",(user_mail,encoded_pwd)) == 1:
        print('login')
    else:
        print('invalid credentials')
user_login(user_mail,password)
