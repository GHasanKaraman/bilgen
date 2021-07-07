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
    pass

def norm(matrix):
    pass