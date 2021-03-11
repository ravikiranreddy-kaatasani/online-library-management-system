"""
search bar
"""
import re
from beautifultable import BeautifulTable
import pymysql


mydb = pymysql.connect(host='localhost', user='root', password='root', database='library')
cursor = mydb.cursor()


def searchbar_book():
    """
    searching for books
    :return:
    """
    try:
        book_column = {'1': 'book_id', '2': 'book_name', '3': 'book_author', '4': 'genre'}
        by_type_b = input("""\nselect by which type you want to search books
                    \r1.book id\t2.book name\t3.book author\t4.genre\t q,Q.to quit\t:""")
        if by_type_b in book_column.keys():
            column_name = book_column[by_type_b]
        elif by_type_b in ('q', 'Q'):
            return
        else:
            print('you selected invalid option\nTry Again:')
            return searchbar_book()
        book_search = "'" + input("enter your data what you want to search:") + "'"
        sql = "SELECT * FROM book where %s REGEXP %s;" % (column_name, book_search)
        cursor.execute(sql)
        output = cursor.fetchall()
        table = BeautifulTable()
        table.field_names = []
        table.columns.header = ["book_id", "book_name", "book_author", "genre"]
        if output:
            for row in output:
                table.rows.append([str(row[0]).ljust(4), str(row[1]).ljust(50), str(row[2]).ljust(40), str(row[3]).ljust(20)])
            print(table)
        else:
            print("Search results not found")
        searchbar_book()
    except Exception:
        print("Techinical error")


def searchbar_user():
    """
           search bar: for user searching
    """
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
        by_type_u = input("""\nselect by which type you want to search user
1.user_id\t2.username\t3.user email\t4. his book id
                        5.his book name\tq,Q.To Quit\t:""")
        user_column = {'1': 0, '2': 1, '3': 2, '4': 3,'5': 4,'6': 5, '7': 6}
        if by_type_u in user_column.keys():
            column_name = user_column[by_type_u]
        elif by_type_u in ('q', 'Q'):
            print("you selected to quit for searching users")
            return True
        else:
            print('you selected invalid option')
            print("Try Again:")
            return searchbar_user()
        text = input("enter your search from user information :")
        search_flag = 0
        table = BeautifulTable()
        table.columns.header = ["User Id", "user Name", "Email Id","His Book Ids","His Book names","His Issue Dates"]

        for i in output:
            if re.search(text.lower(), str(i[column_name]).lower()):
                search_flag = 1
                if i[3] is not None:
                    table.rows.append([str(i[0]), str(i[1]), str(i[2]),str(i[3]), str(i[4]),str(i[5])])
                else:
                    table.rows.append([str(i[0]), str(i[1]), str(i[2]),"no transactions","no transactions",
                                       "no transactions"])
        print(table)
        if search_flag == 0:
            print("Search results not found")
        searchbar_user()

    except Exception :
        print("Technical Error")

#keep options for calling these functions
searchbar_book()
searchbar_user()
