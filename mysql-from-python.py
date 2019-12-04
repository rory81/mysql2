import os
import datetime
import pymysql


# get username
username = os.getenv('C9_USER')

connection = pymysql.connect(
    host='localhost', user=username, password='', db='Chinook')
try:
    # run a query
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'bob']
        # Prepare a string with the same number of placeholders as list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(
            format_strings), list_of_names)
        """
        rows = [('bob', 21, '1990-02-06 23:04:56'),
                ('jim', 56, '1955-05-09 13:12:45'),
                ('fred', 100, '1911-09-12 01:01:01')]
        cursor.executemany("INSERT INTO Friends VALUES(%s,%s,%s);", rows)
        # You must commit() to confirm any changes you make, or rollback to discard them.
        """
        connection.commit()
        # Pure SELECT statements, since they never make any changes to the database, don't have to have their changes committed.
finally:
    # close connection, regardless the outcome of the query
    connection.close()
