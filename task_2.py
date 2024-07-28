import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="112121",
    database="alx_book_store"
)

mycursor= mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS Order_Details")
mycursor.execute("DROP TABLE IF EXISTS Books")
mycursor.execute("DROP TABLE IF EXISTS Authors")
mycursor.execute("DROP TABLE IF EXISTS Orders")
mycursor.execute("DROP TABLE IF EXISTS Customers")



author = '''CREATE  TABLE Authors(
author_id INT PRIMARY KEY,
author_name VARCHAR(215)
)'''

book ='''CREATE TABLE Books(
book_id INT PRIMARY KEY NOT NULL,
title VARCHAR(130) NOT NULL,
author_id INT, 
price DOUBLE,
publication_date DATE
)'''

customer = '''CREATE TABLE Customers(
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL,
    address TEXT
)'''


order ='''CREATE TABLE Orders(
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE
)'''

order_details = ''' CREATE TABLE Order_Details(
orderdetailid INT PRIMARY KEY,
order_id INT,
book_id INT ,
quantity DOUBLE
)'''

mycursor.execute(author)
mycursor.execute(book)
mycursor.execute(customer)
mycursor.execute(order)
mycursor.execute(order_details)





mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)
