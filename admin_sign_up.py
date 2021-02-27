import pymysql
import base64
from re import fullmatch

mydb=pymysql.connect(host='localhost',user='root',password='root',database='library_management_trial')
cursor=mydb.cursor()

admin_name=input('enter user name').strip()
admin_mail= input('enter user mail').strip()
password= input('enter passwordd').strip()

def user_signup(admin_name,admin_mail,password):
    if cursor.execute("select user_mail_id from user_tt where user_mail_id =%s;",(admin_mail)) == 1:
        print('user already exists')
    else:

        if fullmatch("(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}",password):
            encoded_pwd = base64.b64encode(password.encode('ascii'))
            cursor.execute("insert into user_tt (user_name,user_mail_id,password,is_admin_flag) values(%s,%s,%s,%s)",(admin_name,admin_mail,encoded_pwd,1))
            mydb.commit()
            #print('hi')
        else:
            print("--Password did not match the requirements--")
user_signup(admin_name,admin_mail,password)

