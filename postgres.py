# pip install psycopg2-binary

import psycopg2

connect = psycopg2.connect(
       database="python",
       user='morvin',
       password='12345678',
       host='localhost',
       port= '5432'
)

cursor = connect.cursor()

cursor.execute("CREATE TABLE rongo(PersonID int, LastName varchar(255), FirstName varchar(255), Address varchar (255),City varchar(255))")

connect.close()
