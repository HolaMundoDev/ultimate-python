import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO usuarios values(?, ?)",
        (1, "Hola Mundo"),
    )
