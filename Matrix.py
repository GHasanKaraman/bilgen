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

    def __repr__(self):
        single_dimension_of_matrix = []
        for i in self.array:
            for j in i:
                single_dimension_of_matrix.append(j)
                
        area_of_element = len(str(max(single_dimension_of_matrix)))   
                
        a = ''
        for i in self.array:
            a += '['
            for j in i:
                for s in range(area_of_element - len(str(j))):
                    a += ' '
                a += str(j) + ' ' 
            a += ']'
            
            a += '\n '
            
        return '['+a[:len(a)-2]+']' 

    def __iter__(self):
        for i in self.array:
            yield i

    def __getitem__(self, index):
        return self.array[index]
    
    def __setitem__(self, index, value):
        self.array[index] = value