import builtins
from matrix.errors import MatrixError
from matrix.errors import AxisError

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
                
        single_dimension_of_matrix_str_len = []
        
        for i in single_dimension_of_matrix:
            single_dimension_of_matrix_str_len.append(len(str(i)))
            
        max_area = max(single_dimension_of_matrix_str_len)
        
        a = ''
        for i in self.array:
            a += '['
            for j in i:
                if not type(single_dimension_of_matrix[single_dimension_of_matrix_str_len.index(max_area)]) == float:
                    for s in range(max_area - len(str(j))):
                        a += ' '
                a += str(j) + ' ' 
                if type(single_dimension_of_matrix[single_dimension_of_matrix_str_len.index(max_area)]) == float:
                    for s in range(max_area - len(str(j))):
                        a += ' '
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
                temp = []
                sliced_array = self.array[index[0]]
                if not type(sliced_array[0]) == list:
                    sliced_array = [sliced_array]
                for arr in sliced_array:
                    sliced_col = arr[index[1]]
                    if not type(sliced_col) == list:
                        sliced_col = [sliced_col]
                    temp.append(sliced_col)
                sliced_matrix = Matrix(temp)
                if type(value) == Matrix and (sliced_matrix.shape == value.shape):                  
                    index0 = index[0]
                    index1 = index[1]
                    if type(index[0]) == slice:
                        index0 = str(index[0])
                        index0 = index0.split("(")[1:][0]
                        index0 = index0[:len(index0) - 1]
                        index0 = index0.split(",")[:2]
                        index0[0] = index0[0].strip()
                        index0[1] = index0[1].strip()
                        if index0[0] == "None":
                            index0[0] = 0
                        else:
                            index0[0] = int(index0[0])
                        if index0[1] == "None":
                            index0[1] = self.shape[0]
                        else:
                            index0[1] = int(index0[1])
                    if type(index[1]) == slice:
                        index1 = str(index[1])
                        index1 = index1.split("(")[1:][0]
                        index1 = index1[:len(index1) - 1]
                        index1 = index1.split(",")[:2]
                        index1[0] = index1[0].strip()
                        index1[1] = index1[1].strip()
                        if index1[0] == "None":
                            index1[0] = 0
                        else:
                            index1[0] = int(index1[0])
                        if index1[1] == "None":
                            index1[1] = self.shape[1]
                        else:
                            index1[1] = int(index1[1])
                    if type(index0) == list and type(index1) == list:
                        for i in range(index0[0], index0[1]):
                            for j in range(index1[0], index1[1]):
                                self[i, j] = value[i % (index0[1] - index0[0]) , j % (index1[1] - index1[0])]
                    elif type(index0) == list and type(index1) == int:
                        for i in range(index0[0], index0[1]):
                            self[i, index1] = value[i, 0]
                    elif type(index0) == int and type(index1) == list:
                        for i in range(index1[0], index1[1]):
                            self[index0, i] = value[0, i]
                elif type(value) == int or type(value) == float:
                    for i, r in enumerate(sliced_matrix):
                        for j, c in enumerate(r):
                            sliced_matrix[i, j] = value
                    self[index] = sliced_matrix
                else:
                    raise ValueError("could not broadcast input array from shape {} into shape {}".format(value.shape, sliced_matrix.shape))
                    
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

    def __sub__(self, other):
        if type(other) is int or type(other) is float:
            temp = []
            for row in self:
                temp_row = []
                for col in row:
                    temp_row.append(col - other)
                temp.append(temp_row)
            return Matrix(temp)
        else:
            return self.__add(self, other*(-1))
    
    def __rsub__(self, other):
        if type(other) is int or type(other) is float:
            temp = []
            for row in self:
                temp_row = []
                for col in row:
                    temp_row.append(other - col)
                temp.append(temp_row)
            return Matrix(temp)
        else:
            return self.__add(other, self*(-1))

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

    def sum(self, axis = None, keepdims = False):
        matrix = self
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

    def max(self, axis = None, keepdims = False):
        matrix = self
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
                for c in r:
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
                for c in r:
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

    def min(self, axis = None, keepdims = False):
        matrix = self
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