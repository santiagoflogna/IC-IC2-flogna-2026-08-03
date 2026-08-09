peliculas = [
    {
        "titulo": "El secreto de sus ojos",
        "anio": 2009,
        "director": "Juan José Campanella"
    },
    {
        "titulo": "Nueve reinas",
        "anio": 2000,
        "director": "Fabián Bielinsky"
    },
    {
        "titulo": "Relatos salvajes",
        "anio": 2014,
        "director": "Damián Szifron"
    }
]

director_buscado = "Fabián Bielinsky"
encontrada = False

for pelicula in peliculas:
    if pelicula["director"] == director_buscado:
        print(pelicula["titulo"])
        encontrada = True

if encontrada == False:
    print("No se encontraron películas de ese director")