import csv
import os

# Escribir
# with open("archivos/archivo.csv", "w") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow({"twit_id", "user_id", "text"})
#     writer.writerow({1000, 1, "este es un tweet"})
#     writer.writerow({1001, 2, "otro twit!"})

# Leer
# with open("archivos/archivo.csv") as archivo:
#     reader = csv.reader(archivo)
#     print(list(archivo))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)

# Actualizar
with open("archivos/archivo.csv") as r, open("archivos/archivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000, 1, "texto modificado"])
        else:
            writer.writerow(linea)
    os.remove("archivos/archivo.csv")
    os.rename("archivos/archivo_temp.csv", "archivos/archivo.csv")
