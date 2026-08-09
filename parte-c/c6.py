pelicula1 = {
    "titulo": "Dune",
    "anio": 2021
}

pelicula2 = {
    "puntaje": 8,
    "anio": 2024
}

pelicula1.update(pelicula2)

print(pelicula1)

pelicula = pelicula1 | pelicula2

print(pelicula)