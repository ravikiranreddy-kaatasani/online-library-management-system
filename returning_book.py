""""Importing connection, current_date and number_books functions """
from test_prog import connection, current_date


def returned_book():
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
