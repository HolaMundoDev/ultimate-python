from datetime import datetime, timedelta

fecha1 = datetime(2023, 1, 1) + timedelta(weeks=1)
fecha2 = datetime(2023, 2, 1)

delta = fecha2 - fecha1
print(delta)
print("dias", delta.days)
print("segundos", delta.seconds)
print("microsegundos", delta.microseconds)
print("total_seconds()", delta.total_seconds())
