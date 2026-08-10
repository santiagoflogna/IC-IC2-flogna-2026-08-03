import sys

sys.path.append("parte-c")

from c3 import pelicula


def test_duracion_inexistente():
    resultado = pelicula.get("duracion", "desconocido")

    assert resultado == "desconocido"