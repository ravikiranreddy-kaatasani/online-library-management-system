import pymysql
from beautifultable import BeautifulTable
import warnings
warnings.filterwarnings("ignore")
def user_data():
    mydb = pymysql.connect(host='localhost', user='root', password='root', database='library')
    cursor = mydb.cursor()
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
def user_module():
    mydb = pymysql.connect(host='localhost', user='root', password='root', database='library')
    cursor = mydb.cursor()
    data = cursor.execute('select * from user')
    username = input("enter your mail to login:")
    password = input("enter your password to login:")
    for i in cursor:   
        if username in i and password in i:
            print('Hi welcome to Ojas Library management')
            while (True):
                type = input('select option for book search as per your requirement\n1.book id\t2.book name\t3.book author\t4.genere\t:')
                user_column = {'1':"book_id" , '2':"book_name" , '3':"book_author" , '4':"genre"}
                if type in user_column.keys():
                    column_name = user_column[type]
                    break
                else:
                    print("please enter from above options")
            while True:
                book_search = "'" + input("enter your data what you want to search:") + "'"
                sql = "SELECT * FROM book where %s REGEXP %s and number_of_copies>0;" % (column_name, book_search)
                cursor.execute(sql)
                output = cursor.fetchall()
                table1=BeautifulTable()
                if output:
                    for row in output:
                        table1.rows.append([str(row[0]).ljust(4), str(row[1]).ljust(50), str(row[2]).ljust(40), str(row[3]).ljust(20),str(row[4]).ljust(20)])
                    table1.columns.header=["book_id","book_name","book_author","genre","number_of_copies"]
                    print(table1)
                    print("THIS IS THE BOOK LIST WE HAVE IN OUR LIBRARY SELECT WHAT U ")
                    break
                else:
                    print("Search results not found")
                    break
                    
    mydb.close()          
user_module()
user_data()   

