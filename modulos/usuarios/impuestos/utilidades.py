if __name__ != "__main__":
    from usuarios.gestion.crud import guardar

    print(__name__)

    def pagar_impuestos():
        print("pagando impuestos")
        guardar()


if __name__ == "__main__":
    print("tarea de mantenimiento")
