def estadisticas(notas):
    datos = {
        "promedio": promedio(notas),
        "maximo": max(notas),
        "minimo": min(notas)
    }

    return datos

def promedio(notas):
    suma = 0

    for nota in notas:
        suma = suma + nota

    resultado = suma / len(notas)

    return resultado

notas = [7, 4, 9, 10, 6]

print(estadisticas(notas))