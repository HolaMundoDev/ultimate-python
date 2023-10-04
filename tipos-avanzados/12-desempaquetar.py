# lista1 = [1, 2, 3, 4]
# print(*lista)

# lista2 = [5, 6]

# combinada = ["Hola", *lista1, "mundo", *lista2, "chanchito"]
# print(combinada)

punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}

nuevoPunto = {**punto1, "lala": "hola mundo", **punto2, "z": "mundo"}
print(nuevoPunto)
