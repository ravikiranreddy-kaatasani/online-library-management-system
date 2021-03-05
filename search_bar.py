import pymysql
import re
mydb = pymysql.connect(host='localhost', user='root', password='root', database='library')
cursor = mydb.cursor()


def search_bar_user_or_book(searchfor):
    if searchfor == 'book':
        while (True):
            type = input('select by which type you want to search books\n1.book id\t2.book name\t3.book author\t4.genere\t ')
            if type not in "1234":
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
        book_search = "'" + input("enter your data what you want to search:") + "'"
        sql = "SELECT * FROM book where %s REGEXP %s;" % (coloum_name, book_search)
        cursor.execute(sql)
        output = cursor.fetchall()
        if output:
            for row in output:
                print(str(row[0]).ljust(4), str(row[1]).ljust(50), str(row[2]).ljust(40), str(row[3]).ljust(20), sep=" | ")
                break
        else:
            print("Search results not found")

    elif searchfor == 'user':
        try:
            sql = """select 
                                u.user_id,
                                u.user_name,
                                u.mail_id,
                                GROUP_CONCAT(b.book_id SEPARATOR ' ! '),
                                GROUP_CONCAT(b.book_name SEPARATOR '! '),
                                GROUP_CONCAT(t.issue_date SEPARATOR '! ')
                                from user_book_taken t  join book b on t.book_id=b.book_id 
                                                   right join user u on t.user_id=u.user_id 
                                                                                            group by u.user_id;"""
            cursor.execute(sql)  # Execute SQL Query to select all record
            output = cursor.fetchall()  # fetches all the rows in a result1 set
            print(output)
            while (True):
                type = input("select by which type you want to search user\n1.user_id\t2.username\t3.user email\t4. his book id\t5.his book name\t:")
                if type not in "123456":
                    print("please enter from above options", type)
                    continue
                elif type == '1':
                    coloum_name = 0
                    break
                elif type == '2':
                    coloum_name = 1
                    break
                elif type == '3':
                    coloum_name = 2
                    break
                elif type == '4':
                    coloum_name = 3
                    break
                elif type == '5':
                    coloum_name = 4
                    break
                elif type == '6':
                    coloum_name = 5
                    break
            text = input("enter your search for user information :")
            search_flag = 0
            for i in output:
                if re.search(text.lower(), str(i[coloum_name]).lower()):
                    search_flag = 1
                    if i[3]!=None:
                        print(str(i[0]).ljust(4), str(i[1]).ljust(4), str(i[2]).ljust(4), str(i[3]).ljust(4), str(i[4]).ljust(4),str(i[5]).ljust(4), sep=" | ")
                    else:
                        print(str(i[0]).ljust(4), str(i[1]).ljust(4), str(i[2]).ljust(4), "\tThis users has no transactions of books", sep=" | ")
            if search_flag == 0:
                print("search results not found")

        except Exception:
            print('Error:Unable to fetch data.due to technical error')
        finally:
            mydb.close()

search_no=0
while True:
    searchfor = input("enter your search option:\n search for books :book\t to search for users\t:user\tenter (q,quit) to quit: \nenter here search type by \t:")
    searchfor=searchfor.lower()
    search_no=search_no+1
    if searchfor == 'book' or searchfor == 'user':
        search_bar_user_or_book(searchfor)
    elif searchfor == 'quit' or searchfor == 'q':
        print("you have selected to quit")
        break
    else:continue
