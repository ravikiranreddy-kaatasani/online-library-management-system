import pymysql
def user_info():
   mysqldb=pymysql.connect(host="localhost",user="root",password="root",database="library_management_trail")#established connection between your database  
   mycursor=mysqldb.cursor()#cursor() method create a cursor object  
   try:  
      mycursor.execute("select user_id,user_name,total_books_taken from users")#Execute SQL Query to select all record   
      result=mycursor.fetchall() #fetches all the rows in a result set
      #print(result[0][0])
      l=[]
      for i in result:    
         user_id=i[0]
         l.append(i[0])
         user_name=i[1]
         total_books_taken=i[2]
         print(user_id,user_name,total_books_taken)
      #print(l)
      user_input=int(input("Enter User's Id: ")) #Asking user input for retriving particular user
      if user_input in l:            
         mycursor.execute("select u.user_id,us.user_name,b.book_id,b.book_name,b.book_author,u.book_issued_date,u.book_returned_date,u.fine from user_transaction u inner join books b on u.book_id=b.book_id join users us on us.user_id=u.user_id where u.user_id={}".format(user_input))#Execute SQL Query to select all record 
         result1=mycursor.fetchall() #fetches all the rows in a result1 set
         for row in result1:
            user_id=row[0]
            book_id=row[1]
            book_name=row[2]
            book_author=row[3]
            book_issued_date=row[4]
            book_returned_date=row[5]
            fine=row[6]
            print(user_id,book_id,book_name,book_author,book_issued_date,book_returned_date,fine)
      else:
         print("User Id is not available")
   except ValueError as ex:
      print('Enter only valid id')
   except Exception as e :
      print(e)
      
      print('Error:Unable to fetch data.')  
   mysqldb.close()

user_info()
 
