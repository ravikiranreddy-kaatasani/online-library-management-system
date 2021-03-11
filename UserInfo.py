import pymysql 
from beautifultable import BeautifulTable
import warnings
warnings.filterwarnings("ignore")
mydb=pymysql.connect(host="localhost",user="root",password="root",database="library")#established connection between your database  
cursor=mydb.cursor()#cursor() method create a cursor object
def user_info():     
      try:
          cursor.execute("select user_id,user_name,number_of_books_taken,total_fine from user")#Execute SQL Query to select all record   
          result=cursor.fetchall() #fetches all the rows in a result set
          table = BeautifulTable(maxwidth=200)
          table.column_headers = ["UserId", "UserName", "BooksTaken", "TotalFine"]
          for i in result:
              table.append_row(i)
          print(table)    
          while True:   
              print("Enter your Choice for viewing purpose")  
              print("1: view by using user_id")
              print("2: view by using mail_id")
              print("q: press q to quit")
             
              user_input=(input("Enter a number : "))#Asking user input for retriving particular user
             
              if user_input == '1':
                  user_input_1()
                             
              elif user_input == '2':
                  user_input_2()
                  
              elif user_input in ('q','quit'):
                  break
            
              else:
                  print("Enter only 1 or 2 or q")
              
      except Exception as e :
          print(e)
          print('Error:Unable to fetch data.')
              
def user_input_1():
    uid=(input("\nEnter user_id: "))
    cursor.execute("select u.user_id,ubt.user_name,ubt.book_id,b.book_name,ubt.genre,ubt.book_author,ubt.issue_date,ubt.actual_return_date,ubt.user_return_date,ubt.fine from user_book_taken ubt join book b on b.book_id=ubt.book_id join user u on ubt.user_id=u.user_id where u.user_id='%s'"%(uid))#Execute SQL Query to select all record 
    table1 = BeautifulTable(maxwidth=200)
    table1.column_headers = ["UserID", "UserName", "BookID", "BookName", "Genre", "BookAuthor", "IssueDate", "ActualReturnDate", "UserReturnDate", "Fine"]
    result1=cursor.fetchall() #fetches all the rows in a result1 set
    if result1:
        for row in result1:
            table1.append_row(row)
        print(table1) 
    else:
        query  = 'select distinct(u.user_id) from user u join user_book_taken ubt where not  u.user_id = ubt.user_id;'
        cursor.execute(query)
        distinct_raw=cursor.fetchall()
        distinct = tup_tup_to_list(distinct_raw)
        if uid in distinct:
            print("\n\nThe Person has not taken a book till date\n\n")
        else:
            print("Please enter a valid id\n")
            user_input_1()

def user_input_2():
    umail=input("Enter User Mail Id: ")
    umm ="'"+umail+"'"
    cursor.execute("select u.user_id,ubt.user_name,ubt.book_id,b.book_name,ubt.genre,ubt.book_author,ubt.issue_date,ubt.actual_return_date,ubt.user_return_date,ubt.fine from user_book_taken ubt join book b on ubt.book_id=b.book_id join user u on ubt.user_id=u.user_id where ubt.mail_id="+umm+"")#Execute SQL Query to select all record 
    table2 = BeautifulTable(maxwidth=200)
    table2.column_headers = ["UserID", "UserName", "BookID", "BookName", "Genre", "BookAuthor", "IssueDate", "ActualReturnDate", "UserReturnDate", "Fine"]
    result1=cursor.fetchall() #fetches all the rows in a result1 set            
    if result1:
        for row in result1:
            table2.append_row(row)
        print(table2)
    else:
        query  = 'select distinct(u.mail_id) from user u join user_book_taken ubt where not u.mail_id = ubt.mail_id;'
        cursor.execute(query)
        distinct_raw=cursor.fetchall()
        distinct = tup_tup_to_list(distinct_raw)

        if umail in distinct:
            print("He has not taken a book till date")    
        else:
            print("Please enter a valid Mail-id")
            user_input_2()    

def tup_tup_to_list(distinct):
    lis = []
    for i in distinct:
        for j in i:
            lis.append(j)
    return lis
            
user_info()

