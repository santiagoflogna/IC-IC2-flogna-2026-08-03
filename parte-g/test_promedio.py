import sys

sys.path.append("parte-d")

from d1 import promedio


def test_promedio():
    resultado = promedio([7, 4, 9, 10, 6])

    assert resultado == 7.2


#def test_promedio_incorrecto():
    #resultado = promedio([7, 4, 9, 10, 6])

    #assert resultado == 8