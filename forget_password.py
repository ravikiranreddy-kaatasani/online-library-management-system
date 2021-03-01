##import smtplib
#https://www.google.com/settings/security/lesssecureapps

import pymysql
import base64
from re import fullmatch

mydb=pymysql.connect(host='localhost',user='root',password='root',database='library_management_trial')
cursor=mydb.cursor()


def forget_password():
    from random import randint
    from re import fullmatch
    import base64
    import smtplib

    d= [str(randint(1,9)) for i in range(6)]
    otp="".join(d)
    print(otp)
    
    s = smtplib.SMTP('smtp.gmail.com', 587) 
 
    s.starttls() 

    s.login("srustith@gmail.com", input('enter password')) 
      
    message = otp
      
    s.sendmail("srustith@gmail.com","srustith@gmail.com", message) 
    s.quit()
    
    inp=input('enter 6 digit otp')

    if inp == otp:
        new_ps = input('enter new password')
        confirm_password = input('enter confirm password')
        if new_ps == confirm_password:
            if fullmatch("(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}",confirm_password):
                encoded_cn_pwd = base64.b64encode(confirm_password.encode('ascii'))
                print(encoded_cn_pwd)
                query= cursor.execute('update user_tt set password= %s where user_id = %s',(encoded_cn_pwd,20212))
                mydb.commit()
                print('password changed')
            else:
                print('password didnot match requirment(it should contain atleast upper case , lower case, digit and special character)')
        else:
            print('new_password and confirm_password didnot match')
    else:
        print('incorrect OTP')
    
forget_password()
