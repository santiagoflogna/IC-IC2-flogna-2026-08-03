puntajes = [120, 45, 300, 80, 210]

mayor = puntajes[0]
menor = puntajes[0]
suma = 0 

for puntaje in puntajes:
    if puntaje > mayor:
        mayor = puntaje

    if puntaje < menor:
        menor = puntaje

    suma = suma + puntaje 


promedio = suma / len(puntajes)

print("Mayor:", mayor)
print("Menor:", menor)
print("Promedio:", promedio)


print("Mayor con max():", max(puntajes))
print("Menor con min():", min(puntajes))
