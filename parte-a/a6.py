pares = 0
impares = 0


for alumno in range(1, 31):
    if alumno % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

total = pares + impares

print("Cantidad de alumnos pares:", pares)
print("Cantidad de alumnos impares:", impares)
print("Cantidad total de alumnos",total)