import smtplib
import pymysql
from beautifultable import BeautifulTable
import warnings
warnings.filterwarnings("ignore")
mydb = pymysql.connect(host='localhost', user='root', password='root', database='library')
cursor = mydb.cursor()
def user_module():
    cursor.execute('select * from user')
    data=cursor.fetchall()
    user_id=input("enter user_id").lower()
    for i in data:
        if user_id in i:
            cursor.execute('select user_id,book_id,book_name,issue_date,actual_return_date,fine from user_book_taken;')
            dat=cursor.fetchall()
            table=BeautifulTable()
            for j in dat:
                table.rows.append([str(j[0]),str(j[1]),str(j[2]),str(j[3]),str(j[4]),str(j[5])])
            table.columns.header=["user_id","book_id","book_name","issue_date","actual_return_date","fine"]
            print(table)
user_module()

    
