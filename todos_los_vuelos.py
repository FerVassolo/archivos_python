#El fin de este escript es dar un ejemplo claro de como es que buscamos los vuelos
import os
import struct
file_name = "Vuelos"
fpi = open(file_name, "r+b")

file_size = os.path.getsize(file_name)

data = fpi.read()
k = 1
j = 0
for i in range(0, file_size):
# Como todos los numeros guardados en el file son enteros y todos los enteros tienen un tamaño de 8 bit:
# busco cada 8 bits el siguiente nro
# a los 24 bits se que pasamos al siguiente vuelo (cada vuelo tiene 3 elementos de 8 bits cada --> 8*3 = 24)
    if i == 0 or i % 8 == 0:
        if j == 0:
            print(f"VUELO {str(k)}: \nDestino: {str(data[i])}")
        elif j == 1:
            print(f"Capacidad del avion: {str(data[i])}")
        elif j == 2:
            print(f"Numero de pasajeros: {str(data[i])}\n")
            j = 0
            k += 1
            continue
        j += 1
