""" Database connection module
"""
import pymysql
mydb= pymysql.connect(host='localhost',user='root',password='root',database='library')
cursor= mydb.cursor()
