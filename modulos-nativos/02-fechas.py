# import time

# print(time.time())

from datetime import datetime

fecha = datetime(2023, 1, 1)
fecha2 = datetime(2023, 2, 1)

ahora = datetime.now()

fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%d")

print(fecha.strftime("%Y.%m.%d"))
print(fecha > fecha2)

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute
)
