"""It contains current_date, connection and number_books functions"""
import datetime
import pymysql
from issue_book import issue_book
from return_book import returned_book


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


def number_books():
    """User choose the number of books that he want"""
    user_choice = input("Enter your choice, whether you want to take or return the book:")

    if user_choice in ['take', 'return']:

        if user_choice == 'take':
            issue_book()
        else:
            returned_book()
    else:
        print("enter only 'take' or 'return'")
        number_books()


number_books()
