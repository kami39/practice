import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

# retrieve one record
c.execute('SELECT name FROM category ORDER BY sort')
print(c.fetchone())
print(c.fetchone())

print('----------------------------------')
# retrieve all records as a list
c.execute('SELECT * FROM book WHERE book.category=1')
print(c.fetchall())

print('----------------------------------')
# iterate through the records
for row in c.execute('SELECT name, price FROM book ORDER BY sort'):
    print(row)
print('----------------------------------')