import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Chanchito Feliz"),
        (3, "Chanchito Triste")
    ]
    cursor.executemany(
        "INSERT INTO usuarios values(?, ?)",
        usuarios
    )
