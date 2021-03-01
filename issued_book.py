import pymysql

import datetime

date = datetime.datetime.now()

issue_date = date.strftime('%m-%d-%Y')

def issued_book():

    '''Connecting to mysql'''
    
    conn = pymysql.connect(host='localhost',user='root',password='root',db='library_mgmt')
    
    cur = conn.cursor()
    
    cur.execute("SELECT * from request_data")
    
    '''Fetching the data'''
    
    data = cur.fetchall()
    
    cur.execute("select * from users")

    data1 = cur.fetchall()

    cur.execute("select * from users_books_issue")

    data2 = cur.fetchall()

    while True:

        try:

            num = int(input("Enter the number of books you want to take:"))
            
            break

        except ValueError:

            print("Entered number should be integer only")         
        

    for n in range(num):

        while True:
        
            try:
                userid = int(input("Enter the user id:"))
                
                break
                
            except ValueError:
                
                print("user id should be only integers")
                

        username = input("Enter the user name:")

        while True:

            try:
                
                bookid = int(input("Enter the book id:"))

            except ValueError:

                print("book id should be only integers")
            

        print("userid:{},username:{},bookid:{}".format(userid,username,bookid))
        

        for i in data:
            
            if (userid in i) and (username in i) and (bookid in i):

                print(i)

                for j in data1:
                    
                    if (userid in j) and (username in j):

                        #count = "select total_books_taken from users where user_id = %s;"

                        #count_books = cursor.execute(count,userid)

                        #if count_books < 4:

                        for k in data2:
                            
                            if userid in k and bookid in k:

                                print(userid,bookid,k)

                                print("You have already opted this book, you can only opt one book with same id")

                                break
                        
                        else:
                    
                            bookname = input("Enter the book name:")
                            
                            genre = input("Enter the genre name:")
                            
                            issue_date = datetime.datetime.now()

                            issue_date = date.strftime("%Y-%m-%d")
                            
                            print(issue_date)

                            use_data = (userid,username,bookid,bookname,genre,issue_date)
                                
                            query = "Insert into users_books_issue(userid,username,bookid,bookname,genre,issue_date) values(%s,%s,%s,%s,%s,%s);"

                            cur.execute(query,use_data)

                            conn.commit()

                            query1 = "update books set number_of_copies = number_of_copies - 1 where book_id = %s;"

                            cur.execute(query1,bookid)
                            
                            conn.commit()
                            
                            query2 = "update users set total_books_taken = total_books_taken + 1 where user_id = %s;"

                            cur.execute(query2,userid)
                            
                            conn.commit()

                            query3 = "delete from request_data where userid = %s and bookid = %s;"

                            cur.execute(query3,(userid,bookid))
                            
                            conn.close()

                            #break
                        
                        break
        

                else:

                    print("Can't find your details in users")

                    #break
                
                break
            
        else:
            
            print("Can't find your data in request data, first you need to raise a request to borrow the book")

            break

issued_book()
