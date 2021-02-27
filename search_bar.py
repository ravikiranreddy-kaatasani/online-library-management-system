import pymysql
mydb = pymysql.connect(host='localhost', user='root', password='root', database='libarymanagement')
cursor = mydb.cursor()

def search_bar_users(option ):
    if option == 1:
        while(True):
            type = int(input('select by which type you want to search books\n1.book id\t2.book name\t3.book author\t4.genere\t:'))
            if type not in "1234":
                print("please enter from above options")
                continue
            elif str(type) == '1':
                coloum_name = "Book_id"
                break
            elif str(type) == '2':
                coloum_name = "Book_name"
                break
            elif str(type) == '3':
                coloum_name = "Book_author"
                break
            elif str(type) == '4':
                coloum_name = "Genre"
                break
        book_search = "'" + input("enter your data what you want to search:") + "'"
        sql = "SELECT * FROM books where %s REGEXP %s;" % (coloum_name, book_search)
        cursor.execute(sql)
        output = cursor.fetchall()
        for row in output:
           print(str(row[0]).ljust(4) ,str(row[1]).ljust(50), str(row[2]).ljust(40),str(row[3]).ljust(20), sep=" | ")
    elif option == 2:
        user_id = "'" + input("enter your userid to search for data") + "'"
        sql="select u.user_id,us.user_name,b.book_id,b.book_name,b.book_author,u.book_issued_date,u.book_returned_date,u.fine from user_transaction u inner join books b on u.book_id=b.book_id join users us on us.user_id=u.user_id where u.user_id={}".format(user_id)
        cursor.execute(sql)
        output = cursor.fetchall()
        for row in output:
            print(str(row[0]).ljust(4), str(row[1]).ljust(50), str(row[2]).ljust(40), str(row[3]).ljust(20), sep=" | ")
    else:
        print("Invalid search option\n")


option = int(input("enter your search option:\n 1.search for books \t 2.to search for users\t: "))
search_bar_users(option)

