# numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2

comando = ""

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
