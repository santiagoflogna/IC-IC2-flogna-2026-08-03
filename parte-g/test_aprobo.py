import sys

sys.path.append("parte-d")

from d2 import aprobo


def test_aprueba():
    notas = [7, 4, 9, 10, 6]

    assert aprobo(notas) == True


def test_desaprueba():
    notas = [2, 4, 5, 3, 6]

    assert aprobo(notas) == False


def test_aprueba_en_el_limite():
    notas = [6, 6, 6, 6, 6]

    assert aprobo(notas) == True