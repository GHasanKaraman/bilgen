from bilgen.Matrix.Array import Matrix
from bilgen.Matrix.Errors import MatrixError
from bilgen.Matrix.Errors import LinAlgError

def transpose(matrix):
    if type(matrix) == Matrix:
        return matrix.transpose()
    else:
        raise LinAlgError("The given argument must be a Matrix!")

def dot(matrix1, matrix2):
    if type(matrix1) == Matrix and type(matrix2) == Matrix:
        temp = zero(matrix1.shape[0],matrix2.shape[1])
        for i in range(matrix1.shape[0]):
            for k in range(matrix2.shape[1]):
                for j in range(matrix2.shape[0]):
                    temp[i,k] += matrix1[i,j]*matrix2[j,k]             
        return Matrix(temp)
    else:
        raise TypeError("The given argument must be a Matrix!")

def add(matrix1, matrix2):
    if(matrix1.shape == matrix2.shape):
        tmp_matrix = []
        for i in range(matrix1.shape[0]):
            tmp_array = []
            for j in range(matrix1.shape[1]):
                tmp_array.append(matrix1[i,j] + matrix2[i, j])
            
            tmp_matrix.append(tmp_array) 
        
        return Matrix(tmp_matrix)
    else:
        raise LinAlgError("The dimensions of the two given matrices must be the same")

def sub(matrix1, matrix2):
    if(matrix1.shape == matrix2.shape):
        tmp_matrix = []
        for i in range(matrix1.shape[0]):
            tmp_array = []
            for j in range(matrix1.shape[1]):
                tmp_array.append(matrix1[i,j] - matrix2[i, j])
            
            tmp_matrix.append(tmp_array) 
        
        return Matrix(tmp_matrix)
    else:
        raise LinAlgError("The dimensions of the two given matrices must be the same")

def det(matrix):

    if type(matrix) == Matrix:
        r, c = matrix.shape
        if r == c:
            if r == 1:
                return matrix[0, 0]
            elif r == 2:
                T_right = matrix[0, 0] * matrix[1, 1]
                T_left = matrix[0, 1] * matrix[1, 0]
                return T_right - T_left;
            else:
                det_matrix = 0
                for i in range(c):
                    det_matrix += matrix[0, i] * ((-1)**i) * det(ignore(matrix, 0, i))
                return det_matrix
        else:
            raise LinAlgError("The matrix must be square!")
    else:
        raise TypeError("The given argument must be a Matrix!")

def ignore(matrix, row, col):
        new_matrix = []
        for i, r in enumerate(matrix):
            if not i == row:
                new_matrix.append(r)
        temp = []
        for i, row in enumerate(new_matrix):
            temp_row = []
            for j, _ in enumerate(row):
                if not j == col:
                    temp_row.append(new_matrix[i][j])
            temp.append(temp_row)
        return Matrix(temp)

def minor(matrix):
    temp = []
    for i, r in enumerate(matrix):
        temp_row = []
        for j, c in enumerate(r):
            temp_matrix = ignore(matrix, i, j)
            temp_det = det(temp_matrix)
            temp_row.append(temp_det)
        temp.append(temp_row)
    return Matrix(temp)

def cofactor(matrix, isMinor = False):
    new_matrix = matrix
    if not isMinor:
        new_matrix = minor(matrix)
    temp = []
    for i, r in enumerate(new_matrix):
        temp_row = []
        for j, c in enumerate(r):
            coeff = (-1)**(i+j)
            temp_row.append(coeff*new_matrix[i, j])
        temp.append(temp_row)
    return Matrix(temp)

def adjoint(matrix, isCofactor = False):
    new_matrix = matrix
    if not isCofactor:
        new_matrix = cofactor(matrix)
    return transpose(new_matrix)

def inv(matrix):
    coeff = 1/det(matrix)
    print(coeff)
    return adjoint(matrix)*coeff

def norm(matrix):
    pass

def zero(row, col):
    temp = []
    for i in range(row):
        temp_row = []
        for j in range(col):
            temp_row.append(0)
        temp.append(temp_row)
    return Matrix(temp)

def one(row, col):
    pass

def identity():
    pass