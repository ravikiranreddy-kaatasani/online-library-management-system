"""[summary]
"""
import admin
while True:
    print("Hi Admin \n Pls provide credentials to authenticate :")
    try:
    # print("Hi Admin \n Pls provide credentials to authenticate :")
        main_uid = admin.start()
        print(main_uid)
    except Exception as exception_e:
        print('Error', exception_e)
