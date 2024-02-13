import sqlite3

conn = sqlite3.connect('dp_customers.db')
cursor = conn.cursor()

update_query = "UPDATE Customers SET city = 'New City', state = 'New State' WHERE state = 'Florida' AND postal_code = 34110 LIMIT 5"
cursor.execute(update_query)

new_customers = [
    ('Customer1', 'City1', 'State1', '000001'),
    ('Customer2', 'City2', 'State2', '000001'),
    ('Customer3', 'City3', 'State3', '000001'),
    ('Customer4', 'City4', 'State4', '000001'),
    ('Customer5', 'City5', 'State5', '000001'),
    ('Customer6', 'City6', 'Florida', '34110'),
    ('Customer7', 'City7', 'Florida', '34110'),
    ('Customer8', 'City8', 'Florida', '34110'),
    ('Customer9', 'City9', 'Texas', 'TX1'),
    ('Customer10', 'City10', 'Texas', 'TX2'),
    ('Customer11', 'City11', 'Texas', 'TX3'),
    ('Customer12', 'City12', 'State12', '000001'),
    ('Customer13', 'City13', 'State13', '000001'),
    ('Customer14', 'City14', 'State14', '000001'),
    ('Customer15', 'City15', 'State15', '000001')
]

insert_query = "INSERT INTO Customers (name, city, state, postal_code) VALUES (?, ?, ?, ?)"
cursor.executemany(insert_query, new_customers)


conn.commit()
conn.close()


