import sqlite3

con = sqlite3.connect("sqlite/app.db")

cursor = con.cursor()
cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id INTEGER primary key, nombre VARCHAR(50));
    """
)
con.commit()
con.close()
