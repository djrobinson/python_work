import sqlite3

conn = sqlite3.connect("new.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE population
                (city TEXT, state TEST, population INT)
                """)

conn.close()