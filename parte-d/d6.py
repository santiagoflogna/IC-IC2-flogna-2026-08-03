def promedio(notas):
    suma = 0

    for nota in notas:
        suma = suma + nota

    resultado = suma / len(notas)

    return resultado


def estadisticas(notas):
    datos = {
        "promedio": promedio(notas),
        "maximo": max(notas),
        "minimo": min(notas)
    }

    return datos


def reporte(notas):
    datos = estadisticas(notas)

    texto = f"Promedio: {datos['promedio']} | Máximo: {datos['maximo']} | Mínimo: {datos['minimo']}"

    return texto


notas = [7, 4, 9, 10, 6]

print(reporte(notas))