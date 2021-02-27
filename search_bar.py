import pymysql
mydb = pymysql.connect(host='localhost', user='root', password='root', database='libarymanagement')
cursor = mydb.cursor()

def search_bar_users(option ):
    if option == '1':
        while(True):
            type = (input('select by which type you want to search books\n1.book id\t2.book name\t3.book author\t4.genere\t:'))
            if type not in "1234":
                print("please enter from above options")
                continue
            elif type == '1':
                coloum_name = "Book_id"
                break
            elif type == '2':
                coloum_name = "Book_name"
                break
            elif type == '3':
                coloum_name = "Book_author"
                break
            elif type == '4':
                coloum_name = "Genre"
                break
        book_search = "'" + input("enter your data what you want to search:") + "'"
        sql = "SELECT * FROM books where %s REGEXP %s;" % (coloum_name, book_search)
        cursor.execute(sql)
        output = cursor.fetchall()
        if output:
            for row in output:
               print (str(row[0]).ljust(4) ,str(row[1]).ljust(50), str(row[2]).ljust(40),str(row[3]).ljust(20), sep=" | ")
        else:
            print("Search is not found")
    elif option == '2':
        try:
            cursor.execute("select user_id,user_name,total_books_taken from users")  # Execute SQL Query to select all record
            result = cursor.fetchall()  # fetches all the rows in a result set
            l = []
            for i in result:
                l.append(i[0])
            user_id= int(input("Enter User's Id: "))  # Asking user input for retriving particular user
            if user_id in l:
                sql = """select u.user_id,
                us.user_name,
                GROUP_CONCAT(b.book_id SEPARATOR ' , ') as  HisBookids,
                GROUP_CONCAT(b.book_name SEPARATOR ', ') as HisBooknames,
                GROUP_CONCAT(u.book_issued_date SEPARATOR ', ') as HisBookIssueddates
                from user_transaction u inner join books b on u.book_id=b.book_id join users us on us.user_id=u.user_id where u.user_id={}""".format(user_id)
                cursor.execute(sql)  # Execute SQL Query to select all record
                output = cursor.fetchall()  # fetches all the rows in a result1 set
                for row in output:
                    if row[0]!= None:
                        print(str(row[0]).ljust(4), str(row[1]).ljust(50), str(row[2]).ljust(40), str(row[3]).ljust(20),str(row[4]).ljust(20), sep=" | ")
                    else:
                        cursor.execute("select user_id,user_name,total_books_taken from users where user_id={}".format(user_id))
                        user_output = cursor.fetchall()
                        for row in user_output:
                            print(str(row[0]).ljust(4), str(row[1]).ljust(50),str(row[2]).ljust(50), sep=" | ")
                            print("you have no transaction done for books")
            else:
                print("User Id is not available")
        except ValueError:
            print('Enter only User id')
        except Exception:
            print('Error:Unable to fetch data.')
        finally:
            mydb.close()

option = input("enter your search option:\n 1.search for books \t 2.to search for users\t: ")
if option in "12":
    search_bar_users(option)
else:
    print("enter valid option")
