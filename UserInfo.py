import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="root",database="library")#established connection between your database  
cursor=mydb.cursor()#cursor() method create a cursor object
def user_info():
    while True:  
      try:
          cursor.execute("select user_id,user_name,number_of_books_taken,total_fine from user")#Execute SQL Query to select all record   
          result=cursor.fetchall() #fetches all the rows in a result set
          for i in result:
             print(list(i))
            
          print("1: search by using user_id")
          print("2: search by using mail_id")
         
          user_input=int(input("Enter a number : "))#Asking user input for retriving particular user
         
          if user_input == 1:
              user_input_1()
              break
                         
          elif user_input == 2:
              user_input_2()
              break
            
          else:
              print("Enter only 1 or 2")
          
      except ValueError:
          print('Enter only integers')
      except Exception as e :
          print(e)
          print('Error:Unable to fetch data.')
          
    mydb.close()

def user_input_1():
    uid=(input("Enter user_id: "))
    cursor.execute("select u.user_id,ubt.user_name,ubt.book_id,b.book_name,ubt.genre,ubt.book_author,ubt.issue_date,ubt.actual_return_date,ubt.user_return_date,ubt.fine from user_book_taken ubt join book b on b.book_id=ubt.book_id join user u on ubt.user_id=u.user_id where u.user_id='%s'"%(uid))#Execute SQL Query to select all record 
    result1=cursor.fetchall() #fetches all the rows in a result1 set
    if result1:
        for row in result1:
            print(row)
        
    else:
        print("Please enter a valid id")
        user_input_1()

def user_input_2():
    umail=input("Enter User Mail Id: ")
    umm ="'"+umail+"'"
    cursor.execute("select u.user_id,ubt.user_name,ubt.book_id,b.book_name,ubt.genre,ubt.book_author,ubt.issue_date,ubt.actual_return_date,ubt.user_return_date,ubt.fine from user_book_taken ubt join book b on ubt.book_id=b.book_id join user u on ubt.user_id=u.user_id where ubt.mail_id="+umm+"")#Execute SQL Query to select all record 
    result1=cursor.fetchall() #fetches all the rows in a result1 set
            
    if result1:
        for row in result1:
            print(row)

    else:
        print("Please enter a valid Mail-id")
        user_input_2()    
        

user_info()
 
