def promedio(notas):
    suma = 0

    for nota in notas:
        suma = suma + nota

    resultado = suma / len(notas)

    return resultado


def aprobo(notas):
    if promedio(notas) >= 6:
        return True
    else:
        return False


notas1 = [7, 4, 9, 10, 6]
notas2 = [2, 1, 5, 3, 8]

print("Notas 1:", aprobo(notas1))
print("Notas 2:", aprobo(notas2))