import sys

sys.path.append("parte-d")

from d3 import estadisticas


def test_estadisticas():
    notas = [7, 4, 9, 10, 6]

    resultado = estadisticas(notas)

    assert resultado["promedio"] == 7.2
    assert resultado["maximo"] == 10
    assert resultado["minimo"] == 4