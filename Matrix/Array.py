from bilgen.Matrix.Errors import MatrixError

class Matrix:
    def __init__(self, array):
        col = 0
        if type(array[0]) is list:
            col = len(array[0])
        else:
            raise MatrixError("Creating a matrix from ragged nested sequences (which is a list matrices with different lengths or shapes) is deprecated.")
        for item in array:
            if type(item) is list:
                if not len(item) == col:
                    raise MatrixError("Creating a matrix from ragged nested sequences (which is a list matrices with different lengths or shapes) is deprecated.")
            else:
                raise MatrixError("Creating a matrix from ragged nested sequences (which is a list matrices with different lengths or shapes) is deprecated.")
        self.array = array
        self.shape = (self.__row(), self.__col())

    def __repr__(self):
        single_dimension_of_matrix = []
        for i in self.array:
            for j in i:
                single_dimension_of_matrix.append(j)
                
        max_num_area = len(str(max(single_dimension_of_matrix)))   
        min_num_area = len(str(min(single_dimension_of_matrix)))   
                
        a = ''
        for i in self.array:
            a += '['
            for j in i:
                for s in range(max([max_num_area,min_num_area]) - len(str(j))):
                    a += ' '
                a += str(j) + ' ' 
            a += ']'
            
            a += '\n '
            
        return '['+a[:len(a)-2]+']' 

    def __iter__(self):
        for i in self.array:
            yield i

    def __len__(self):
        return len(self.array)

    def __getitem__(self, index):
        l = 0
        if type(index) == tuple:
            l = len(index)
        if l > 2:
            raise IndexError("too many indices for matrix: matrix is 2-dimensional, but {} were indexed".format(l))
        elif l == 2:
            if type(index[0]) == int and type(index[1]) == int:
                return self.array[index[0]][index[1]]
            else:
                temp = []
                sliced_array = self.array[index[0]]
                if not type(sliced_array[0]) == list:
                    sliced_array = [sliced_array]
                for arr in sliced_array:
                    sliced_col = arr[index[1]]
                    if not type(sliced_col) == list:
                        sliced_col = [sliced_col]
                    temp.append(sliced_col)
                return Matrix(temp)               
        else:
            return self.array[index]
    
    def __setitem__(self, index, value):
        l = 0
        if type(index) == tuple:
            l = len(index)
        if l > 2:
            raise IndexError("too many indices for matrix: matrix is 2-dimensional, but {} were indexed".format(l))
        elif l == 2:
            if type(index[0]) == int and type(index[1]) == int:
                self.array[index[0]][index[1]] = value
            else:
                pass               
        else:
            self.array[index] = value

    def __add(self, matrix1, matrix2):
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
            raise MatrixError("The dimensions of the matrices must be proportional")

    def __add__(self, other):
        if type(other) is int or type(other) is float:
            temp = []
            for row in self:
                temp_row = []
                for col in row:
                    temp_row.append(col + other)
                temp.append(temp_row)
            return Matrix(temp)
        else:
            return self.__add(self, other)
    
    def __radd__(self, other):
        if type(other) is int or type(other) is float:
            temp = []
            for row in self:
                temp_row = []
                for col in row:
                    temp_row.append(col + other)
                temp.append(temp_row)
            return Matrix(temp)
        else:
            return self.__add(self, other)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            temp = []
            for row in self:
                temp_row = []
                for col in row:
                    temp_row.append(col * other)
                temp.append(temp_row)
            return Matrix(temp)
    
    def __rmul__(self, other):
        if type(other) == int or type(other) == float:
            temp = []
            for row in self:
                temp_row = []
                for col in row:
                    temp_row.append(col * other)
                temp.append(temp_row)
            return Matrix(temp)

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            temp = []
            for row in self:
                temp_row = []
                for col in row:
                    temp_row.append(col / other)
                temp.append(temp_row)
            return Matrix(temp)
    
    def __rtruediv__(self, other):
        if type(other) == int or type(other) == float:
            temp = []
            for row in self:
                temp_row = []
                for col in row:
                    temp_row.append(other / col)
                temp.append(temp_row)
            return Matrix(temp)

    def __pow__(self,other):
        if type(other) == int or type(other) == float:
            temp = []
            for row in self:
                temp_row = []
                for col in row:
                    temp_row.append(col ** other)
                temp.append(temp_row)
            return Matrix(temp)
    
    def __rpow__(self,other):
        if type(other) == int or type(other) == float:
            temp = []
            for row in self:
                temp_row = []
                for col in row:
                    temp_row.append(other**col)
                temp.append(temp_row)
            return Matrix(temp)

    def __row(self):
        return len(self.array)

    def __col(self):
        return len(self.array[0])
    
    def transpose(self):
        tmp_matrix = []
        for i in range(self.shape[1]):
            tmp_array = []
            for j in self:
                tmp_array.append(j[i])
            
            tmp_matrix.append(tmp_array) 
        
        return Matrix(tmp_matrix)