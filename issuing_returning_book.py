"""It contains current_date, connection and number_books functions"""
import datetime
import pymysql
#from issuing_book import issue_book
#from returning_book import returned_book


def current_date():
    """Getting the current date for issuing the book and actual actual return date"""
    date = datetime.datetime.now()
    issue_date = date.strftime("%Y-%m-%d")
    print(issue_date)
    actual_return_date = date + datetime.timedelta(days = 15)
    actual_return_date = actual_return_date.strftime("%Y-%m-%d")
    print(actual_return_date)
    return issue_date, actual_return_date


def connection():
    """Connecting to mysql"""
    mydb = pymysql.connect(host='localhost', user='root', password='root', db='library')
    cursor = mydb.cursor()
    cursor.execute("select * from user")
    user_data = cursor.fetchall()
    cursor.execute("SELECT * from request_issue_return where "
                "request_issue_date is NOT NULL and request_return_date is NULL")
    request_issue_data = cursor.fetchall()
    cursor.execute("SELECT * from request_issue_return where request_return_date is NOT NULL")
    request_return_data = cursor.fetchall()
    cursor.execute("select * from user_book_taken")
    user_taken_book_data = cursor.fetchall()
    print("Connection established")
    return mydb, cursor, user_data, request_issue_data, request_return_data, user_taken_book_data

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def issue_book():
    """Admin issuing the books to the user"""
    mydb, cursor, user_data, request_issue_data, \
    request_return_data, user_taken_book_data = connection()
    while True:
        try:
            num = int(input("Enter the number of books you want to take:"))
            if isinstance(num, int):
                if num > 3:
                    print("You can't take more than 3 books")
                elif num < 3:
                    break
        except ValueError:
            print("Entered number should be integer only")
    print(num)
    issue_date, actual_return_date = current_date()
    while num > 0:
        userid = input("Enter the user id:").lower().strip()
        while True:
            try:
                bookid = int(input("Enter the book id:"))
                break
            except ValueError:
                print("book id should be only integers")
        print("userid:{}, bookid:{}".format(userid, bookid))
        for i in request_issue_data:
            if (userid in i) and (bookid in i):
                print(i)
                for j in user_data:
                    if userid in j:
                        print(j)
                        print("hi")
                        cursor.execute("select request_issue_date from "
                                       "request_issue_return where user_id_no = %s "
                                       "and book_id_no = %s;", (userid, bookid))
                        request_issue_date = cursor.fetchall()
                        cursor.execute("select book_name from book where book_id = %s;", bookid)
                        bookname = cursor.fetchall()
                        #print(bookname)
                        cursor.execute("select book_author from book where book_id = %s;", bookid)
                        bookauthor = cursor.fetchall()
                        cursor.execute("select genre from book where book_id = %s;", bookid)
                        genre = cursor.fetchall()
                        mail_id = "select mail_id from user where user_id = %s;"
                        cursor.execute(mail_id, userid)
                        mailid = cursor.fetchall()
                        #print(mailid)
                        query = "select user_name from user where user_id = %s;"
                        cursor.execute(query, userid)
                        username = cursor.fetchall()
                        user_insert_data = (userid,  bookid, mailid, username,
                                            bookname, bookauthor, genre, request_issue_date,
                                            issue_date, actual_return_date)
                        query = "Insert into user_book_taken(user_id, book_id, mail_id, " \
                                "user_name, book_name, book_author, " \
                                "genre,request_issue_date, issue_date, actual_return_date) " \
                                "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                        cursor.execute(query, user_insert_data)
                        mydb.commit()
                        query1 = "update book set number_of_copies = number_of_copies - 1 " \
                                 "where book_id = %s;"
                        cursor.execute(query1, bookid)
                        mydb.commit()
                        query2 = "update user set number_of_books_taken = " \
                                 "number_of_books_taken + 1 where user_id = %s;"
                        cursor.execute(query2, userid)
                        mydb.commit()
                        print("connection about to close")
                        break
                else:
                    print("Can't find your details in users")
                break
        else:
            print("Can't find your details in the request table")
        num -= 1
    mydb.close()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def return_book():
    """Admin issuing the books to the user"""
    mydb, cursor, user_data, request_issue_data, \
    request_return_data, user_taken_book_data = connection()
    while True:
        try:
            num = int(input("Enter the number of books you want to return:"))
            int_check = isinstance(num, int)
            if int_check is True:
                if num > 3:
                    print("You can't take more than 3 books")
                elif num < 3:
                    break
        except ValueError:
            print("Entered number should be integer only")
    issue_date, actual_return_date = current_date()
    while num > 0:
        userid = input("Enter the user id:").lower().strip()
        while True:
            try:
                bookid = int(input("Enter the book id:"))
                break
            except ValueError:
                print("book id should be only integers")
        print("userid:{}, bookid:{}".format(userid, bookid))
        for i in request_return_data:
            if (userid in i) and (bookid in i):
                print(i)
                for j in user_data:
                    if userid in j:
                        query = "update user set number_of_books_taken = " \
                                "number_of_books_taken - 1 " \
                                "where user_id = %s;"
                        cursor.execute(query, userid)
                        mydb.commit()
                        query1 = "update user_book_taken set user_return_date = %s " \
                                "where user_id = %s and book_id = %s;"
                        cursor.execute(query1, (issue_date, userid, bookid))
                        mydb.commit()
                        query2 = "update book set number_of_copies = number_of_copies + 1 " \
                                "where book_id = %s;"
                        cursor.execute(query2, bookid)
                        mydb.commit()
                        query3 = "delete from request_issue_return where " \
                                "user_id_no = %s and book_id_no = %s;"
                        cursor.execute(query3, (userid, bookid))
                        mydb.commit()
                        break
                else:
                    print("Can't find your details in users")
                break
        else:
            print("Can't find your details in the request table")
        num -= 1
        print("connection about to close")
    mydb.close()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    

def number_books():
    """User choose the number of books that he want"""
    user_choice = input("Enter your choice, whether you want to take or return the book:")

    if user_choice in ['take', 'return']:

        if user_choice == 'take':
            issue_book()
        else:
            return_book()
    else:
        print("enter only 'take' or 'return'")
        number_books()


number_books()
