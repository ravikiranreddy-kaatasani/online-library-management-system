import pymysql

def insert_update_data():
    
    '''Connecting ot mysql'''
    
    conn = pymysql.connect(host='localhost',user='root',password='root',db='library_mgmt')
    
    cur = conn.cursor()
    
    cur.execute("SELECT * from books")
    
    '''Fetching the data'''
    
    data = cur.fetchall()
    
    while True:
        
        '''Taking input from user whether he/she wants to insert the data or not'''
        
        user_input = input("Please let us know whether you want to insert the values or not, enter only either yes or no:").lower().strip()

        '''If the user input is yes'''
        
        if user_input == "yes": 
            
            try:
                
                '''Admin need to tell how many columns he/she wants to insert'''

                while True:
                    try:
                
                        num = int(input("Enter the number of different books that you want to insert:"))

                        break

                    except:

                        print("Enter only integer values [0-9]\n")

                for i in range(num):
                    
                    bookname = input("Enter the book_name:") 
                   
                    bookauthor = input("Enter the book_author:")

                    bookgenre = input("Enter the Genre:")

                    while True:

                        try:
                            
                            copies = int(input("Enter the number of copies:"))

                            break

                        except:

                            print("Enter only integer values [0-9]")
                    
                    for j in data:
                        
                        '''Checking whether the bookname, bookauthor and bookgenre is already in table or not'''
                        
                        if (bookname in j) and (bookauthor in j) and (bookgenre in j):
                            
                            '''If bookname, bookauthor and bookgenre are already in table then update the number_of_copies in the table'''
                            
                            data = (copies,bookname,bookauthor,bookgenre)
                            
                            try:
                                
                                query = "update books set number_of_copies = number_of_copies + %s where book_name = %s and book_author = %s and genre = %s;"
                                
                                cur.execute(query,data)
                                
                                conn.commit()
                                
                                break
                            
                            except:
                                
                                conn.rollback()

                    
                    else:

                        """If bookname, bookauthor and bookgenre are not in table then we need to insert the values in the table after entering the bookid."""

                        while True:

                            try:
                                
                                bookid = int(input("Enter the book id:"))

                                break

                            except:

                                print("Book id shoub should be integer only [0-9]")
                        
                        data1 = (bookid,bookname,bookauthor,bookgenre,copies)
                        
                        try:
                            
                            query = "Insert into books(book_id,book_name,book_author,genre,number_of_copies) values(%s,%s,%s,%s,%s);"
                            
                            cur.execute(query,data1)
                            
                            conn.commit()
                            
                            print(data1)
                    
                        except:
                            
                            conn.rollback()  

                conn.close()
                
            except ValueError:
                
                print("Oops!  That was not a valid number. Enter only integers")
                
        elif user_input == "no":
            
            break
        
        else:
            
            print("enter either yes or no only")
            
insert_update_data()
