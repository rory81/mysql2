import os
import pymysql

# get username
username = os.getenv('C9_USER')

connection = pymysql.connect(
    host='localhost', user=username, password='', db='Chinook')
try:
    # run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()  # fetchall to retrieve data
        print(result)
finally:
    # close connection, regardless the outcome of the query
    connection.close()
