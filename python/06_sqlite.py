import sqlite3

def CUSTOMER():

    connection = sqlite3.connect("chinook1.db")


    cursor = connection.execute("""select FirstName,LastName 
                                FROM customers
                                where FirstName like 'a%'  """)

    for row in cursor:
        print("FirstName =" + row[0] )
        print("LastNAme = " + row[1] )
        print("Address = " + row[1] )
        print("******************************")

    connection.close()


def insertCustomer():
    connection = sqlite3.connect("chinook1.db")

    connection.execute("""insert into customers 
                       (firstName,lastName,City,Email)
                       values ('Engin', 'demiroğ', 'ankara', 'rahmet42tr@gmail.com'  ) """)
    
    connection.close()


def updatecustomer():
    connection = sqlite3.connect("chinook1.db")

    connection.execute("""update customers  set City= 'İSTANBUL' 
                       where City='Paris' """)
    
    connection.close()
    
def delete():
    connection = sqlite3.connect("chinook1.db")
    connection.execute("""Delete from customers
                       where CustomerId=2 """)
    
    connection.close()

delete()

CUSTOMER()
insertCustomer()
updatecustomer()