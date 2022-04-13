import os
import struct
file_name = "Vuelos"
fpi = open(file_name, "r+b")

file_size = os.path.getsize(file_name)

data = fpi.read()

k = 1
j = 0

# INCISO (a)

destinos =[]
for i in range(0,16):
    destinos.append([i+1, []])

for i in range(0, file_size):
    if i == 0 or i % 8 == 0:
        if j == 0:
            destino = data[i]
        elif j == 1:
            capacidad = data[i]
        elif j == 2:
            pasajeros =data[i]
            j = 0
            k += 1
            destinos[destino -1][1].append(pasajeros*100/capacidad)
            continue
        j += 1

print("(a) Promedio de pasajeros respecto a la capacidad del avion por destino (en porcentaje)")
for destino in destinos:
    total = 0
    i = 0
    if len(destino[1]) != 0:
        for promedio in destino[1]:
            total += promedio
            i += 1
        print(str(destino[0]) + ": " + str(total/i))

# INCISO (b)

# vamos a reciclar parte del (a): por cada porcentaje en destinos[destino[1]] significa q hubo un vuelo

file_destinos = f"Destinos"
if os.path.exists(file_destinos):
    fp = open(file_destinos, "r+b")
else:
    fp = open(file_destinos, "w+b")

formato = "ll"
for elemento in destinos:
    destino = elemento[0]
    cantidad_de_vuelos = 0
    for promedio in elemento[1]:
        cantidad_de_vuelos +=1
    contenido = struct.pack(formato, destino, cantidad_de_vuelos)
    fp.write(contenido)

    # Para visualizarlo, vamos a imprimir cada destino
    n = struct.calcsize(formato)
    var = struct.unpack(formato, contenido)
    print(var)




