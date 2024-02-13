import sqlite3

connection = sqlite3.connect('dp_customers.db')
cursor = connection.cursor()

query = 'INSERT INTO Customers (name, city, state, postal_code) VALUES (?, ?, ?, ?)'

first = ('Steve Something', 'Some City', 'A far away land', '84044')
second = ('Steve Somethings brother', 'Some City', 'A far away land', '84044')
third = ('Steve Somethings sister', 'Some City', 'A far away land', '84044')
fourth = ('Steve Somethings brother from another mother', 'Some City', 'A far away land', '84044')

cursor.execute(query, first)
cursor.execute(query, second)
cursor.execute(query, third)
cursor.execute(query, fourth)

connection.commit()
connection.close()
