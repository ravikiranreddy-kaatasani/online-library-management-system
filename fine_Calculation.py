import pymysql
from datetime import date
from datetime import datetime
mydb=pymysql.connect(host='localhost',user='root',password='root',database='finecalc')
cursor=mydb.cursor()
def fine_Calculation():
    data=cursor.execute('select user_id,book_issued_date,book_returned_date from user_transaction ')

    dt=cursor.fetchall()
    #print(dt)
    #print(dt[0][0])
    issue_date=dt[0][1]
    #print(issue_date)
    return_date=dt[0][2]
    #print(return_date)
    #print(i)
    for k in dt:
        #print(k)
        no_of_days=k[2]-k[1]
        n_days=no_of_days.days
        #print(n_days)
        dead_line=15
        fine=n_days-dead_line
        if n_days > dead_line:
            last_fine=fine*5
            print("fine",last_fine)
            dd=cursor.execute('update user_transaction set fine={} where user_id={}'.format(last_fine,k[0]))
            cursor.execute('select fine from user_transaction ')
            mydb.commit()
            cur=cursor.fetchall()
            #break
        '''else:
            print("no due")
            dd=cursor.execute('update user_transaction set fine={} where user_id={}'.format(0,k[0]))
            cursor.execute('select fine from user_transaction ')
            mydb.commit()
            cur=cursor.fetchall()
    '''
