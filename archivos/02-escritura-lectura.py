from pathlib import Path

archivo = Path("archivos/archivo-prueba.txt")
texto = archivo.read_text("utf-8").split("\n")
texto.insert(0, "Hola mundo!")
archivo.write_text("hola mundo", "utf-8")
