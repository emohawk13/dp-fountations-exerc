import sqlite3

connection = sqlite3.connect('dp_customers.db')
cursor = connection.cursor()

rows = cursor.execute("SELECT name, city, state, postal_code FROM Customers")

columns = ['Name', 'City', 'State', 'Postal Code']


for i in rows:
    print(i)