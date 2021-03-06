"""[summary]
"""
import base64
import pymysql
import valid

def start():
    """[summary]
    """
    mydb = pymysql.connect(host='localhost', user='root', password='root', database='library')
    cursor = mydb.cursor()
    uid = input('enter user id').strip().lower()
    uid = valid.userid(uid)
    user_name = input('enter user name :').strip().ljust(30)
    user_mail = input('enter user mail :').strip().ljust(30)
    user_mail = valid.email_validation(user_mail)
    password = input('enter password :').strip().ljust(30)
    password =  valid.password_validation(password)
    user_signup(uid,user_name, user_mail, password,cursor,mydb)

def user_signup(uid, user_name, user_mail, password, cursor, mydb):
    """[summary]

    Args:
        uid ([type]): [description]
        user_name ([type]): [description]
        user_mail ([type]): [description]
        password ([type]): [description]
        cursor ([type]): [description]
        mydb ([type]): [description]
    """
    try:
        query = "select mail_id from user where mail_id =%s or user_id =%s;"
        if cursor.execute(query, (user_mail,uid)) == 1:
            print('user already exists')
        else:
            encoded_pwd = base64.b64encode(password.encode('ascii'))
            query = "insert into user (user_id,user_name,mail_id,password) values(%s,%s,%s,%s)"
            cursor.execute(query,(uid,user_name, user_mail, encoded_pwd))
            mydb.commit()
            print("User Creation Successful")
    except Exception as exception_e:
        print("Error",exception_e)
    finally:
        mydb.close()
        