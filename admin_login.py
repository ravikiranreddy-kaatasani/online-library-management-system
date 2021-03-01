import pymysql
import base64
import re

mydb=pymysql.connect(host='localhost',user='root',password='root',database='library_management_trail')
cursor=mydb.cursor()

admin_mail= input('enter admin mail ')
password= input('enter password ')

def admin_login(admin_mail,password):
    try:
        admin_mail = admin_mail.strip()
        pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        res = re.match(pattern,admin_mail)

        if res :
            encoded_pwd = base64.b64encode(password.encode('ascii'))

            if cursor.execute("select user_id from user_tt where user_mail_id =%s and password =%s and is_admin_flag = %s;",(admin_mail,encoded_pwd,1)) == 1:
                print('admin login')
                #return cursor.fetchall()[0][0])
            else:
                print('invalid credentials')
        else:
            print('Input valid mail id')
    except Exception as e:
        print("Error",e)
admin_login(admin_mail,password)
