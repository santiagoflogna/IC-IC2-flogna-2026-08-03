puntajes = [120, 45, 300, 80, 210]

puntajes_mayores_a_100 = []

for puntaje in puntajes:
    if puntaje > 100:
        puntajes_mayores_a_100.append(puntaje)

print("Lista original:", puntajes)
print("Lista nueva:", puntajes_mayores_a_100)

