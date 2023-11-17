from pathlib import Path
# import db
# import graphql
# import api

# dependencias = {
#     "db": db,
#     "api": graphql,
#     "graphql": api
# }

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": "base de datos",
    "api": "esta es la api",
    "graphql": "esto es graphql"
}


def load(p):
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("el paquete no tiene función init")


list(map(load, paths))
