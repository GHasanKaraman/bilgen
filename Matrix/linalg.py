from bilgen.Matrix.Array import Matrix
from bilgen.Matrix.Errors import MatrixError
from bilgen.Matrix.Errors import LinAlgError

def transpose(matrix):
    if type(matrix) == Matrix:
        return matrix.transpose()
    else:
        raise LinAlgError("The given argument must be a Matrix!")

def dot(matrix1, matrix2):
    pass

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
    
def inv(matrix):
    pass

def det(matrix):
    def __slice(matrix, col):
        new_matrix = matrix[1:]
        temp = []

        for i, row in enumerate(new_matrix):
            temp_row = []
            for j, cl in enumerate(row):
                if not j == col:
                    temp_row.append(new_matrix[i][j])
            temp.append(temp_row)
        return Matrix(temp)
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
                    det_matrix += matrix[0, i] * ((-1)**i) * det(__slice(matrix, i))
                return det_matrix
        else:
            raise LinAlgError("The matrix must be square!")
    else:
        raise TypeError("The given argument must be a Matrix!")
        
def norm(matrix):
    pass