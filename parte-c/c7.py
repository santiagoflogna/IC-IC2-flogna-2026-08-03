frase = "la pelota no se mancha no la mancha a la pelota"

palabras = frase.split()

contador = {}

for palabra in palabras:
    if palabra in contador:
        contador[palabra] = contador[palabra] + 1
    else:
        contador[palabra] = 1

print(contador)