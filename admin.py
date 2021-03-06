"""
Admin _module
"""
import base64
import pymysql
import valid
def start():
    """[summary]

    Returns:
        [type]: [description]
    """
    admin_mail = input('enter admin mail ')
    valid.email_validation(admin_mail)
    password = input("Enter you password")
    mydb = pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           database='library')
    cursor = mydb.cursor()
    return admin_login(admin_mail, password, cursor)
def admin_login(admin_mail, password, cursor):
    """[summary]

    Args:
        admin_mail ([type]): [description]
        password ([type]): [description]
        mydb ([type]): [description]
        cursor ([type]): [description]

    Returns:
        [type]: [description]
    """
    encoded_pwd = base64.b64encode(password.encode('ascii'))
    query = "select user_id from user where mail_id =%s and password =%s and is_admin_flag = %s;"
    if cursor.execute(query,(admin_mail, encoded_pwd, '1')) == 1:
        print('admin login')
        admin_uid = cursor.fetchone()
        # print(admin_uid[0], 's')
        return admin_uid[0]
        # return cursor.fetchall()[0][0])
    print('invalid credentials')
        