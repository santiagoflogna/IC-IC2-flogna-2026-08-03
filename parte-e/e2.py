archivo = open("parte-e/peliculas.csv", "r")

archivo.readline()

suma = 0

for linea in archivo:
    datos = linea.strip().split(",")

    puntaje = int(datos[2])

    suma = suma + puntaje

archivo.close()

print("Suma de puntajes:", suma)