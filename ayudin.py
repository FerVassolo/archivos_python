import os
import struct

# en este file vamos a "crear" 2000 viajes.

file_name = "Vuelos"
if os.path.exists(file_name):
    fpi = open(file_name, "r+b")
else:
    fpi = open(file_name, "w+b")

formato = "lll"

destino = 3
capacidad = 6
pasajeros = 118

contenido = struct.pack(formato, destino, capacidad, pasajeros)
contenido2 = struct.pack(formato, destino, capacidad, 45)

fpi.write(contenido)
fpi.write(contenido2)
n = struct.calcsize(formato)

var = struct.unpack(formato, contenido)
var2 = struct.unpack(formato, contenido2)
print(var)
print(var2)

fpi.close()
