import pymysql
import base64
import re

mydb = pymysql.connect(host='localhost', user='root', password='root', database='library_mgmt')
cursor = mydb.cursor()

admin_name = input('enter user name ').strip()
admin_mail = input('enter user mail ').strip()
password = input('enter password ').strip()

def check(mail):
    mail = mail.strip()
    pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    res = re.match(pattern,mail)
    return  res

def user_signup(admin_name, admin_mail, password):
    try:
        if cursor.execute("select user_mail_id from users where user_mail_id =%s;", (admin_mail)) == 1:
            print('user already exists')
        else:
            if check(admin_mail):
                if fullmatch("(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}", password):
                    encoded_pwd = base64.b64encode(password.encode('ascii'))
                    cursor.execute("insert into user_tt (user_name,user_mail_id,password,is_admin_flag) values(%s,%s,%s,%s)",
                                   (admin_name, admin_mail, encoded_pwd, 1))
                    mydb.commit()
                    print('hi')
                else:
                    print("--Password did not match the requirements--")
            else:
                print("Input valid mail id")
    except Exception as e:
        print("Error",e)

user_signup(admin_name, admin_mail, password)
