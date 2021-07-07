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
        return self.array[index]
    
    def __setitem__(self, index, value):
        self.array[index] = value

    def __row(self):
        return len(self.array)

    def __col(self):
        return len(self.array[0])