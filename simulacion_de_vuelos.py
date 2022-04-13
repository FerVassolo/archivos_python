import os
import struct
import random

# en este file vamos a "crear" 2000 viajes aleatorios.

file_name = "Vuelos"
if os.path.exists(file_name):
    fpi = open(file_name, "r+b")
else:
    fpi = open(file_name, "w+b")

formato = "lll"
i = 0
while i < 2000:
    destino = random.randint(1, 16)
    capacidad = random.randint(110, 225)
    pasajeros = random.randint(0, capacidad)
    contenido = struct.pack(formato, destino, capacidad, pasajeros)
    fpi.write(contenido)
    i += 1

fpi.close()
