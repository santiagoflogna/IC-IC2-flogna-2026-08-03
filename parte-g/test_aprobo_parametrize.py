import sys
import pytest

sys.path.append("parte-d")

from d2 import aprobo


@pytest.mark.parametrize("notas, esperado", [
    ([7, 4, 9, 10, 6], True),
    ([2, 4, 5, 3, 6], False),
    ([6, 6, 6, 6, 6], True)
])
def test_aprobo_varios_casos(notas, esperado):
    assert aprobo(notas) == esperado