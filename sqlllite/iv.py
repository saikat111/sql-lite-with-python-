import sqlite3
conn = sqlite3.connect('img.db')

m = conn.execute("""
SELECT * FROM MY_TABLE
""")
for x in m:
    s =x[2]

with open('ss.jpg','wb') as ss:
    ss.write(s)

conn.commit()
conn.close()