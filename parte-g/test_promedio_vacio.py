import sys

sys.path.append("parte-d")

from d5 import promedio


def test_promedio_lista_vacia():
    resultado = promedio([])

    assert resultado == 0