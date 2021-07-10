from matrix.array import Matrix
from matrix.errors import LinAlgError

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
        raise TypeError("The given arguments must be a Matrix!")

def add(matrix1, matrix2):
    if type(matrix1) == Matrix and type(matrix2) == Matrix:
        return matrix1 + matrix2
    else:
        raise TypeError("The given arguments must be a Matrix!")

def sub(matrix1, matrix2):
    if type(matrix1) == Matrix and type(matrix2) == Matrix:
        return matrix1 + (matrix2 * (-1))
    else:
        raise TypeError("The given arguments must be a Matrix!")

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
        for j in range(len(r)):
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
        for j in range(len(r)):
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

def norm(matrix, axis= None, keepdims = False):
    if type(matrix) == Matrix:
        matrix = matrix**2  
        if axis == None: 
            if keepdims == False: 
                return sum(matrix)**(1/2)
            else: 
                return sum(matrix, keepdims= True)**(1/2)
        elif axis == 0:
            if keepdims == False: 
                temp = sum(matrix, axis = 0)
                for i,k in enumerate(temp):
                    temp[i] = k**(1/2)
                return temp
            else: 
                return sum(matrix, axis = 0, keepdims=True)**(1/2)
        elif axis == 1:
            if keepdims == False: 
                temp = sum(matrix, axis = 1)
                for i,k in enumerate(temp):
                    temp[i] = k**(1/2)
                return temp
            else: 
                return sum(matrix, axis = 1, keepdims= True)**(1/2)
    else:
        raise TypeError("The given argument must be a Matrix!")

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
    if type(matrix) == Matrix:
        return matrix.max(axis, keepdims)
    else:
        raise LinAlgError("The given argument must be a Matrix!")

def min(matrix, axis = None, keepdims = False):
    if type(matrix) == Matrix:
        return matrix.min(axis, keepdims)
    else:
        raise LinAlgError("The given argument must be a Matrix!")

def sum(matrix, axis = None, keepdims = False):
    if type(matrix) == Matrix:
        return matrix.sum(axis, keepdims)
    else:
        raise LinAlgError("The given argument must be a Matrix!")

def vdot(matrix1, matrix2):
   temp = 0
   for i, r in enumerate(matrix1):
      for j, c in enumerate(r):
         temp += c*matrix2[i, j]
   return temp

def qr(matrix):
   m, n = matrix.shape
   Q = zero(m, n)
   R = zero(n, n)
   for j in range(n):
      v = matrix[:, j]
      for i in range(j - 1):
         q = Q[:, i]
         R[i, j] = vdot(q, v)
         v = v - R[i, j] * q
      norm_v = norm(v)
      Q[:, j] = v / norm_v
      R[j, j] = norm_v
   return Q, R