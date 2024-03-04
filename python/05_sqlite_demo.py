import sqlite3

connection = sqlite3.connect("chinook1.db")


cursor = connection.execute("select FirstName,LastName,Address FROM customers")

for row in cursor:
    print("FirstName =" + row[0] )
    print("LastNAme = " + row[1] )
    print("Address = " + row[0] )
    print("******************************")

connection.close()