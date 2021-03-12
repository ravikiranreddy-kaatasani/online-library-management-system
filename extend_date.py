def to_extend():  
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import datetime
    import pymysql
    import cryptography
    mydb = pymysql.connect(host='localhost', user='root', password='root', db='library')
    cursor = mydb.cursor()
    cursor.execute("select user_id, book_id, issue_date, actual_return_date from user_book_taken;")
    query = cursor.fetchall()
    

    user_id = input("Enter the user id:")
    while True:
        try:
            book_id = int(input("Enter the book id:"))
            if isinstance(book_id,int):
                break
        except ValueError:
            print("Book id is in integer only")

    current_date = datetime.datetime.now()
    current_date = current_date.strftime('%Y-%m-%d')
    print(current_date)
    query = "select issue_date from user_book_taken where user_id = %s and book_id = %s and user_return_date is NULL;"
    cursor.execute(query,(user_id,book_id))
    data = cursor.fetchone()
    issue_date = list(data)[0]
    print(issue_date)
    issue_date = data[0]

    query = "select DATEDIFF(%s, %s) from user_book_taken where user_id = %s and book_id = %s ;"
    cursor.execute(query,(current_date,issue_date,user_id, book_id))
    data1 = cursor.fetchone()
    diff_dates = list(data1)[0]

    cursor.execute("select * from user;")
    user_data = cursor.fetchall()

    query = "select actual_return_date from user_book_taken where user_id = %s and book_id = %s and user_return_date is NULL;"
    cursor.execute(query,(user_id,book_id))
    data2 = cursor.fetchone()
    actual_return_date = list(data2)[0]
    print(actual_return_date)

    actual_return_date += datetime.timedelta(days=7)
    print(actual_return_date)

    cursor.execute("select extend_request_date from request_issue_return where user_id = %s and book_id = %s and return_request_date is NULL;",(user_id, book_id))
    extend_date = cur.fetchall()
    print(extend_date)
    

    def credentials():
        sender_address = input("Enter your mail id:")
        sender_pass = input("Enter your password:")
        for user in user_data:
            if sender_address in user and sender_pass in user:
                sender_address = input("Enter your mail id:")           #sender_address = 'ojas.python@gmail.com'
                sender_pass = input("Enter your password:")             #sender_pass = 'Ojas@1525'
                receiver_address = input("Enter receiver's mail id:")   #receiver_address = 'reddyravikiran29@gmail.com'
                return sender_address, sender_pass, receiver_address
        else:
            print("Invalid Credentials")
            credentials()
    try:    
        def send_mail():
            sender_address, sender_pass, receiver_address = credentials()
            #Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'RE: Your extend date request.'   #The subject line
            #The body and the attachments for the mail
            message.attach(MIMEText(mail_content, 'plain'))
            #Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(sender_address, sender_pass) #login with mail_id and password
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
           

        if diff_dates <= 15:
            mail_content ='We accepted your request and your return date is extended.' 
            query = "update user_book_taken set actual_return_date = %s where user_id = %s and book_id = %s;"
            cursor.execute(query,(actual_return_date,user_id,book_id))
            mydb.commit()
            
            cursor.execute("select extend_request_date from request_issue_return where user_id = %s and book_id = %s and return_request_date is NULL;")
            extend_date = cur.fetchall()
            extend_date = list(extend_date)
            extend_date = extend_date[0]

            query = "update user_book_taken set extend_request_date = %s weher book_id = %s and user_id = %s and user_return_date is not NULL;"
            cursor.execute(query,(extend_date,user_id,book_id))
            
            mydb.commit()
            send_mail()
            print('Mail Sent to user by accepting the mail')
         else:
            mail_content ='We can\'t accept your request because you have already crossed your actual_return_date, you have to submit the book, if you want it you can take after returning the book.'
            send_mail()
            print('Mail Sent to user by rejecting the mail')
    except smtplib.SMTPAuthenticationError:
        print("SMTP User authentication error, Email not sent!"):
        
   

to_extend()
