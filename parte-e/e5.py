archivo = open("parte-e/peliculas.csv", "r")

archivo.readline()

sumas = {}
cantidades = {}

for linea in archivo:
    datos = linea.strip().split(",")

    puntaje = int(datos[2])
    genero = datos[3].strip()

    if genero in sumas:
        sumas[genero] = sumas[genero] + puntaje
        cantidades[genero] = cantidades[genero] + 1
    else:
        sumas[genero] = puntaje
        cantidades[genero] = 1

archivo.close()

promedios = {}

for genero in sumas:
    promedios[genero] = sumas[genero] / cantidades[genero]

print(promedios)