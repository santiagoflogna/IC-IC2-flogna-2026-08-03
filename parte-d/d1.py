def promedio(notas):
    suma = 0

    for nota in notas:
        suma = suma + nota

    resultado = suma / len(notas)

    return resultado


notas1 = [7, 4, 9, 10, 6]
notas2 = [2, 1, 5, 3, 8]

print("Promedio 1:", promedio(notas1))
print("Promedio 2:", promedio(notas2))