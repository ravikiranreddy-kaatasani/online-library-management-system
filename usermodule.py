import pymysql
import smtplib
from email.message import EmailMessage
from datetime import datetime

def user_module():
    
    mydb=pymysql.connect(host='localhost',user='root',password='root',database='library')
    cursor=mydb.cursor()

    data = cursor.execute('select * from users')

    username= input('Enter user id  :')
    password= input('Enter password :')

    for i in cursor:   
        if username in i and password in i:
            print('Hi welcome to Ojas Libary management')
            
            def user():
                print("type borrow for request book:")
                print("type return for return book:")
                userinput=input("enter your option:").lower().strip()
                
                try:
                    if userinput=="borrow":
                        
                        try:
                            while True:
                                try:
                                    userid=int(input("Enter your userid:"))
                                    break
                                except ValueError as v:
                                    print("User_id should be integer only")
                
                            bookname=input("Enter book name :")
                            while True:
                                try:
                                    bookid=int(input("Enter book id:"))
                                    break
                                except ValueError as v:
                                    print("bookid should be integer only")
                                
                    
                            date=datetime.today()
                            user_request_date=date.date()

                            fromaddr = input("Enter  your mail_id to send a request:").strip()
                            password = input("Enter your mail password:")
                                                                           
                            
                            message= "i want to borrow a book : \n my username is : {0}\n user id is : {1}\n book name is : {2}\n bookid is : {3}".format(username,userid,bookname,bookid)
                         
                            msg=EmailMessage()
                            msg["Subject"]="Request book"
                            msg["From"]=username
                            msg["To"]="sathishpatel415@gmail.com"
                            msg.set_content(message)
                            
                            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
                            server.login(fromaddr,password)
                            server.send_message(msg)
                            server.quit()
                            
            
                            insert_stmt = "INSERT INTO request_book(userid, email, bookname, bookid,user_request_date) VALUES (%s, %s, %s, %s,%s);"
                            data = (userid, username,bookname,bookid,user_request_date)

                            data1 = cursor.execute(insert_stmt, data)
                            mydb.commit()

                        except BaseException as msg:
                            print("Enter a valid credentials",msg)
                            
                       
                            
                    elif userinput=="return":
                
                        try:
                            while True:
                                try:
                                    userid=int(input("Enter your userid:"))
                                    break
                                except ValueError as v:
                                    print("User_id should be integer only")
                
                            bookname=input("Enter book name :")
                            while True:
                                try:
                                    bookid=int(input("Enter book id:"))
                                    break
                                except ValueError as v:
                                    print("bookid should be integer only")
                                
                        
                            date=datetime.today()
                            user_return_date=date.date()
                            
                            fromaddr =input("Enter  your mail_id to send a request:")
                            password = input("Enter your password:")
                            
                            message = "i want to return a book : \n my username is : {0}\n user id is : {1}\n book name is : {2}\n bookid is : {3}".format(username,userid,bookname,bookid)
                            
                           
                            msg=EmailMessage()
                            msg["Subject"]="Return book"
                            msg["From"]=username
                            msg["To"]="sathishpatel415@gmail.com"
                            msg.set_content(message)
                            
                            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
                            server.login(fromaddr,password)
                            server.send_message(msg)
                            server.quit()
                            

                            insert_stmt = "INSERT INTO return_book(userid, email, bookname, bookid,user_return_date) VALUES (%s, %s, %s, %s,%s);"
                            data = (userid, username,bookname,bookid,user_return_date)
                            data1 = cursor.execute(insert_stmt, data)
                            mydb.commit()

                            
                        except BaseException as msg:
                            print("Enter a valid credentials",msg)

                      

                    else:
                        print("Choose a valid option")
                      
                except BaseException as e:
                    print("enter a valid details",e)
            user()
            break
    
               
    else:
        print('Invalid credintials')
user_module()
