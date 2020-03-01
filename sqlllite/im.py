import sqlite3
conn = sqlite3.connect('img.db')

conn.execute("""
    CREATE TABLE IF NOT EXISTS MY_TABLE 
    (ID INT PRIMARY KEY,
    NAME            TEXT,
    PIC             BLOP
    )

""")

conn.commit()
conn.close()

