archivo = open("parte-e/peliculas.csv", "r")

archivo.readline()

cantidad = 0
suma_puntajes = 0
mejor_puntaje = -1
mejor_pelicula = ""

for linea in archivo:
    datos = linea.strip().split(",")

    titulo = datos[0]
    puntaje = int(datos[2])

    cantidad = cantidad + 1
    suma_puntajes = suma_puntajes + puntaje

    if puntaje > mejor_puntaje:
        mejor_puntaje = puntaje
        mejor_pelicula = titulo

archivo.close()

promedio = suma_puntajes / cantidad

print("Cantidad de películas:", cantidad)
print("Puntaje promedio:", promedio)
print("Mejor puntuada:", mejor_pelicula)