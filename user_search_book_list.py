import smtplib
import pymysql
def user_module():
    mydb = pymysql.connect(host='localhost', user='root', password='root', database='library')
    cursor = mydb.cursor()
    data = cursor.execute('select * from user')
    username = input('Enter your mail id  :')
    password = input('Enter your password :')
    for i in cursor:   
        if username in i and password in i:
            print('Hi welcome to Ojas Library management')
            while (True):
                type = input('select by which type you want to search books\n1.book id\t2.book name\t3.book author\t4.genere\t:')
                if type not in "1234q":
                    print("please enter from above options")
                    continue
                elif type == '1':
                    coloum_name = "book_id"
                    break
                elif type == '2':
                    coloum_name = "book_name"
                    break
                elif type == '3':
                    coloum_name = "book_author"
                    break
                elif type == '4':
                    coloum_name = "genre"
                    break
            while True:
                book_search = "'" + input("enter your data what you want to search:") + "'"
                sql = "SELECT * FROM book where %s REGEXP %s and number_of_copies>0;" % (coloum_name, book_search)
                cursor.execute(sql)
                output = cursor.fetchall()
                if output:
                    for row in output:
                        print(str(row[0]).ljust(4), str(row[1]).ljust(50), str(row[2]).ljust(40), str(row[3]).ljust(20),str(row[4]).ljust(20), sep=" | ")
                    print("this is the booklist we have select any book u want")
                    break
                else:
                    print("Search results not found SERH FOR ANOTHER BOOK")
                    break
                    
    mydb.close()          
user_module()
           
