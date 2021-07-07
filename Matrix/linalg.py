from bilgen.Matrix.Array import Matrix
from bilgen.matrix.Errors import MatrixError

def transpose(matrix):
    if type(matrix) == Matrix:
        return matrix.transpose()
    else:
        raise MatrixError("The given argument must be a Matrix!")

def dot(matrix1, matrix2):
    pass

def add(matrix1, matrix2):
    pass

def sub(matrix1, matrix2):
    pass

def inv(matrix):
    pass

def det(matrix):
    pass

def norm(matrix):
    pass