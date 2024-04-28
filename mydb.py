import mysql.connector

dataBase = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    passwd= '',
    database='semester2'
)

# cursor = dataBase.cursor()
# cursor.execute("Create DATABASE semester2")

print("all done!")
