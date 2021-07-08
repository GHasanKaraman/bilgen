import pytest
from matrix.array import Matrix
import matrix.linalg as lg

a = Matrix([[1, 2], [3, 4]])
b = Matrix([[1, 5], [3, 4]])

@pytest.mark.parametrize('x, result', [
    (a, "[[1 2 ]\n [3 4 ]]"),
    (b, "[[1 5 ]\n [3 4 ]]")
])
def test_str(x, result):
    assert str(x) == result

@pytest.mark.parametrize('x, y, result', [
    (a, 3, Matrix([[4, 5], [6, 7]])),
    (a, b, Matrix([[2, 7], [6, 8]]))
])
def test_add(x, y, result):
    assert (x+y).array == result.array

@pytest.mark.parametrize('x, result', [
    (a, Matrix([[4, 3], [2, 1]])),
    (b, Matrix([[4, 3], [5, 1]]))
])
def test_minor(x, result):
    assert lg.minor(x).array == result.array
