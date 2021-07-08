from bilgen.matrix.array import Matrix
import bilgen.matrix.linalg as lg
import pytest

a = Matrix([[1, 2], [3, 4]])

@pytest.mark.parametrize('x, result', [
    (a, -2)
])

def test_det(a, result):
    assert lg.det(a) == result