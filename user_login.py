"""[summary]

    Returns:
        [type]: [description]
"""
import base64
import pymysql
import valid

def user_login(user_mail,password,cursor,mydb):
    """[summary]

    Args:
        user_mail ([type]): [description]
        password ([type]): [description]
        cursor ([type]): [description]
        mydb ([type]): [description]

    Returns:
        [type]: [description]
    """
    try:
        if valid.email_validation(user_mail):
            encoded_pwd = base64.b64encode(password.encode('ascii'))
            query= "select user_id from user where mail_id =%s and password =%s;"
            if cursor.execute(query,(user_mail,encoded_pwd)) == 1:
                user_id = cursor.fetchone()
                return  user_id[0]
            print('invalid credentials')
        print("Enter valid mail")
    except Exception as exception_e:
        print("Error", exception_e)
    finally:
        mydb.close()
def start():
    """[summary]

    Returns:
        [type]: [description]
    """
    mydb= pymysql.connect(host='localhost',user='root',password='root',database='library')
    cursor= mydb.cursor()
    user_mail= input('enter user mail')
    password= input('enter passwordd')
    return user_login(user_mail,password,cursor,mydb)
