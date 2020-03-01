import sqlite3
conn = sqlite3.connect('img.db')
NAME = 'sunny'
with open('sy.jpg', 'rb') as f:
    PIC = f.read()

conn.execute("""
INSERT INTO MY_TABLE (NAME,PIC) VALUES (?,?)
""",(NAME, PIC))
conn.commit()
conn.close()