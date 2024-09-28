import sqlite3
import base64

conn = sqlite3.connect('images.sqlite')

c = conn.cursor()
c.execute('SELECT * FROM images')
rows = c.fetchall()

for index, row in enumerate(rows):
    print(f"{index}. {row[0]}")