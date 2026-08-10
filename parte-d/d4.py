def promedio(notas):
    suma = 0

    for nota in notas:
        suma = suma + nota

    resultado = suma / len(notas)

    return resultado


def aprobo(notas, minimo=6):
    if promedio(notas) >= minimo:
        return True
    else:
        return False


notas = [7, 4, 9, 8, 6]

print(aprobo(notas))
print(aprobo(notas, minimo=7))