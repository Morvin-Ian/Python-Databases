
# pip install mysql-connector-python
from mysql.connector import (connection)

connect = connection.MySQLConnection(user='root', password='your password',
                                 host='localhost',
                                 database='employees')


cursor = connect.cursor()

cursor.execute("CREATE TABLE Chuka(PersonID int, LastName varchar(255), FirstName varchar(255), Address varchar(255),City varchar(255))")

connect.close()
