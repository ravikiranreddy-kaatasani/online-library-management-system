'''
search
'''

import re
import pymysql


My_db = pymysql.connect(host='localhost', user='root', password='root', database='library')
cursor = My_db.cursor()


def search_bar_book():
    '''
    search bar: for book searching  1.'you have to select by which coloum you want to select book' and next 2.'enter string that you want to search for in select from coloum'
    '''
    try:
        while True:
            by_type = input("""\nselect by which type you want to search books
            \r1.book id\t2.book name\t3.book author\t4.genre\t q,Q.to quit\t:""")
            if by_type == '1':
                column_name = "book_id"
            elif by_type == '2':
                column_name = "book_name"
            elif by_type == '3':
                column_name = "book_author"
            elif by_type == '4':
                column_name = "genre"
            elif by_type in ('q', 'Q'):
                print("you selected to quit for searching books")
                start()
            else:
                print('you selected invalid option\nTry Again:')
                continue
            break
        book_search = "'" + input("enter your data what you want to search:") + "'"
        sql = "SELECT * FROM book where %s REGEXP %s;" % (column_name, book_search)
        cursor.execute(sql)
        output = cursor.fetchall()
        if output:
            for row in output:
                print(str(row[0]).ljust(4), str(row[1]).ljust(50),
                      str(row[2]).ljust(40), str(row[3]).ljust(20), sep=" | ")
        else:
            print("Search results not found")
    except Exception as error:
        print("exception is:", error)


def search_bar_user():
    '''
           search bar: for user searching  1.'you have to select by which coloum you want to get user' and 2.'enter string that you want to search for in that coloum'
    '''
    try:
        sql = """select u.user_id,u.user_name,u.mail_id,
                GROUP_CONCAT(b.book_id SEPARATOR ' ! '),
                GROUP_CONCAT(b.book_name SEPARATOR '! '),
                GROUP_CONCAT(t.issue_date SEPARATOR '! ')
                from user_book_taken t  join book b on 
                t.book_id=b.book_id 
                right join user u on t.user_id=u.user_id 
                group by u.user_id;"""
        cursor.execute(sql)
        output = cursor.fetchall()
        while True:
            by_type = input("""select by which type you want to search user
                        \n1.user_id\t2.username\t3.user email\t4. his book id\t
                        5.his bookname\tq,Q.To Quit\t:""")
            if by_type == '1':
                column_name = 0
            elif by_type == '2':
                column_name = 1
            elif by_type == '3':
                column_name = 2
            elif by_type == '4':
                column_name = 3
            elif by_type == '5':
                column_name = 4
            elif by_type == '6':
                column_name = 5
            elif by_type in ('q', 'Q'):
                print("you selected to quit for searching users")
                start()
            else:
                print('you selected invalid option')
                print("Try Again:")
                continue
            break
        print(column_name)
        text = input("enter your search for user information :")
        search_flag = 0
        for i in output:
            if re.search(text.lower(), str(i[column_name]).lower()):
                search_flag = 1
                if i[3] is not None:
                    print(str(i[0]).ljust(4), str(i[1]).ljust(4), str(i[2]).ljust(4),
                          str(i[3]).ljust(4), str(i[4]).ljust(4),str(i[5]).ljust(4), sep=" | ")
                else:
                    print(str(i[0]).ljust(4), str(i[1]).ljust(4), str(i[2]).ljust(4),
                          "\tThis users has no transactions of books", sep=" | ")
        if search_flag == 0:
            print("search results not found")
    except Exception as error:
        print("exception is",error)

def start():
    '''
    start function
    '''
    option = input("\nEnter option 1:book 2.user:")
    while True:
        if option == "1":
            search_bar_book()
        elif option == "2":
            search_bar_user()
        elif option in ('q','Q'):
            break
        else:
            print(" can only select 1 or 2 or q or Q")
            print("try again")
            start()


start()
