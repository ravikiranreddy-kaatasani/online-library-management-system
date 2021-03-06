import smtplib
from email.message import EmailMessage
import pymysql
import datetime
mydb = pymysql.connect(host='localhost', user='root', password='root', database='library')
cursor = mydb.cursor()
def user_module():
    cursor.execute('select * from user')
    data=cursor.fetchall()
    user_id=input("enter user_id")
    for i in data:
        if user_id in i:
            cursor.execute('select user_id,book_id,book_name,issue_date,actual_return_date,fine from user_book_taken;')
            dat=cursor.fetchall()
            for j in dat:
                print(j[0],j[1],j[2],j[3],j[4],j[5],sep= " | ")

user_module()

    
