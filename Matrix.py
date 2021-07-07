from bilgen.Errors import MatrixError

class Matrix:
    def __init__(self, array):
        row = len(array)
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
        self.T = self.__T()

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
        self.array[index] = value

    def __row(self):
        return len(self.array)

    def __col(self):
        return len(self.array[0])
    
    def __T(self):
        tmp_matrix = []
        for i in range(self.shape[1]):
            tmp_array = []
            for j in self:
                tmp_array.append(j[i])
            
            tmp_matrix.append(tmp_array) 
        
        return tmp_matrix