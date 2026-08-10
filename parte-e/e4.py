archivo = open("parte-e/peliculas.csv", "r")
nuevo_archivo = open("parte-e/filtradas.csv", "w")

archivo.readline()

nuevo_archivo.write("titulo,anio,puntaje,genero\n")

genero_buscado = "drama"

for linea in archivo:
    datos = linea.strip().split(",")

    genero = datos[3].strip()

    if genero == genero_buscado:
        nuevo_archivo.write(linea)

archivo.close()
nuevo_archivo.close()