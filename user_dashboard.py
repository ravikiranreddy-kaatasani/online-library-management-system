


'''
from validate_email import validate_email
print(validate_email("example@gmail.com"))
'''
'''
import smtplib
try:
    sender_email="sathishpatel415@gmail.com"
    rec_email="frendlysathish@gmail.com"
    password=input(str("plese enter your password:"))
    message="hi this is sathish"
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email,password)
    print("login success")
    server.sendmail(sender_email,rec_email,message)
    print("email has been sent to",rec_email)
except BaseException as msg:
    print("error",msg)
    print("type",msg.__class__)
'''

import smtplib
try:
    fromaddr = 'ojas.python@gmail.com'  
    toaddrs  = 'fayaz.shaik6897@gmail.com'  
    msg = "happy bithday"
    username = 'ojas.python@gmail.com'  
    password = 'Ojas@1525'

    server = smtplib.SMTP('smtp.gmail.com', 587)  
    #server.ehlo()
    server.starttls()
    server.login(username, password)  
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
except BaseException as msg:
    print("error",msg)
    print("type",msg.__class__)

   
'''    
import smtplib 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login("ojas.python@gmail.com", "Ojas@1525") 

# message to be sent 
message = "Message_you_need_to_send"

# sending the mail 
s.sendmail("ojas.python@gmail.com", "sathishpatel415@gmail.com", message) 

# terminating the session 
s.quit() 


import smtplib


# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login("classroommanagementapp@gmail.com", "ojas@1525") 

# message to be sent 
message = "hi ravi kiran this malik"

# sending the mail 
s.sendmail("classroommanagementapp@gmail.com", "reddyravikiran29@gmail.com", message) 

# terminating the session 
s.quit() 
'''
