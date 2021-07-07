from bilgen.Matrix.Array import Matrix
from bilgen.Matrix.Errors import AxisError
from bilgen.Matrix.Errors import LinAlgError
import builtins

def transpose(matrix):
    if type(matrix) == Matrix:
        return matrix.transpose()
    else:
        raise LinAlgError("The given argument must be a Matrix!")

def dot(matrix1, matrix2):
    if type(matrix1) == Matrix and type(matrix2) == Matrix:
        if matrix1.shape[1] == matrix2.shape[0]:
            temp = zero(matrix1.shape[0],matrix2.shape[1])
            for i in range(matrix1.shape[0]):
                for k in range(matrix2.shape[1]):
                    for j in range(matrix2.shape[0]):
                        temp[i,k] += matrix1[i,j]*matrix2[j,k]             
            return Matrix(temp)
        elif matrix1.shape[0] == matrix2.shape[0] and matrix1.shape[1] == matrix2.shape[1]:
            temp = zero(matrix1.shape[0],matrix1.shape[1])
            for i in range(matrix1.shape[0]):
                for j in range(matrix1.shape[1]):
                        temp[i,j] = matrix1[i,j]*matrix2[i,j]
            return Matrix(temp)
        else:
            raise LinAlgError("ValueError: shapes ({},{}) and ({},{}) not aligned: {} (dim 1) != {} (dim 0)".format(matrix1.shape[0],matrix1.shape[1],matrix2.shape[0],matrix2.shape[1],matrix1.shape[1],matrix2.shape[0]))
    else:
        raise TypeError("The given argument must be a Matrix!")

def add(matrix1, matrix2):
    if matrix1.shape[0] + matrix1.shape[1] < matrix2.shape[0] + matrix2.shape[1]:        
        matrix1, matrix2 = matrix2, matrix1
        
    if (matrix1.shape == matrix2.shape):
        tmp_matrix = []
        for i in range(matrix1.shape[0]):
            tmp_array = []
            for j in range(matrix1.shape[1]):
                tmp_array.append(matrix1[i,j] + matrix2[i, j])
            
            tmp_matrix.append(tmp_array) 
        
        return Matrix(tmp_matrix)
    elif (matrix1.shape[0] % matrix2.shape[0] == 0 and matrix1.shape[1] % matrix2.shape[1] == 0):
        row_mult = int(matrix1.shape[0] / matrix2.shape[0])
        col_mult = int(matrix1.shape[1] / matrix2.shape[1])
                
        tmp_matrix = matrix1.array
        
        for x in range(row_mult):
            for y in range(col_mult):
                for i in range(matrix2.shape[0]):
                    for j in range(matrix2.shape[1]):
                        tmp_matrix[i + matrix2.shape[0] * x][j + matrix2.shape[1] * y] += matrix2.array[i][j]
                   
        return Matrix(tmp_matrix)
    else:         
        raise LinAlgError("The dimensions of the matrices must be proportional")

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
    temp = []
    for i in range(row):
        temp_row = []
        for j in range(col):
            temp_row.append(1)
        temp.append(temp_row)
    return Matrix(temp)

def identity(size):
    temp = zero(size, size)
    for i in range(size):
        temp[i, i] = 1
    return temp

def max(matrix, axis = None, keepdims = False):
    if axis == None:
        maximum = matrix[0, 0]
        for r in matrix:
            for c in r:
                if maximum < c:
                    maximum = c
        if keepdims:
            return Matrix([[maximum]])
        return maximum
    elif axis == 0:
        maximum = []
        matrix = matrix.transpose()
        for i, r in enumerate(matrix):
            temp_max = r[0]
            for j, c in enumerate(r):
                if temp_max < c:
                    temp_max = c
            maximum.append(temp_max)
        if keepdims:
            return Matrix([maximum])
        return maximum

    elif axis == 1:
        maximum = []
        for i, r in enumerate(matrix):
            temp_max = r[0]
            for j, c in enumerate(r):
                if temp_max < c:
                    temp_max = c
            maximum.append(temp_max)
        if keepdims:
            temp_matrix = []
            for i in maximum:
                temp_matrix.append([i])
            return Matrix(temp_matrix)
        return maximum
    else:
        raise AxisError("axis {} is out of bounds for matrix of dimension 2".format(axis))


def min(matrix, axis = None, keepdims = False):
    if axis == None:
        minimum = matrix[0, 0]
        for r in matrix:
            for c in r:
                if minimum > c:
                    minimum = c
        if keepdims:
            return Matrix([[minimum]])
        return minimum
    elif axis == 0:
        minimum = []
        matrix = matrix.transpose()
        for i, r in enumerate(matrix):
            temp_min = r[0]
            for j, c in enumerate(r):
                if temp_min > c:
                    temp_min = c
            minimum.append(temp_min)
        if keepdims:
            return Matrix([minimum])
        return minimum

    elif axis == 1:
        minimum = []
        for i, r in enumerate(matrix):
            temp_min = r[0]
            for j, c in enumerate(r):
                if temp_min > c:
                    temp_min = c
            minimum.append(temp_min)
        if keepdims:
            temp_matrix = []
            for i in minimum:
                temp_matrix.append([i])
            return Matrix(temp_matrix)
        return minimum
    else:
        raise AxisError("axis {} is out of bounds for matrix of dimension 2".format(axis))

def sum(matrix, axis = None, keepdims = False):
    if axis == None:
        tmp = 0
        for i in matrix:
            for j in i:
                tmp += j
                
        return tmp if keepdims == False else Matrix([[tmp]])
    elif axis == 0:
        tmp = []
        for i in range(matrix.shape[1]):
            tmp.append(0)
            
        for i in matrix:
            for j in range(matrix.shape[1]):
                tmp[j] += (i[j])
                
        return tmp if keepdims == False else Matrix([tmp])
    
    elif axis == 1:
        tmp = []
        for i in matrix:
            tmp.append(builtins.sum(i)) 
        
        if keepdims == False:
            return tmp
        else:
            tmp2 = []
            for i in range(matrix.shape[0]):
                tmp2.append([tmp[i]])
            return Matrix(tmp2)