import sqlite3
import base64
import os
import time

SAVE_PATH = os.path.join(os.getcwd(), 'images')
DB_PATH = './images.sqlite'

conn = sqlite3.connect(DB_PATH)

c = conn.cursor()
c.execute('SELECT * FROM images')
rows = c.fetchall()

def reftime(str_ftime, re_format='%Y%m%d_%H%M'):
    return time.strftime(re_format, time.strptime(str_ftime, '%Y-%m-%d %H:%M'))

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

for index, row in enumerate(rows):
    with open(os.path.join(SAVE_PATH, f"{reftime(row[1])}.jpg"), 'wb') as f:
        f.write(base64.b64decode(row[2]))