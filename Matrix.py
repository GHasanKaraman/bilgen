class Matrix:
    def __init__(self, array):
        self.array = array

    def __repr__(self):
        single_dimension_of_matrix = []
        for i in self.array:
            for j in i:
                single_dimension_of_matrix.append(j)
                
        area_of_element = len(str(max(single_dimension_of_matrix)))   
        print()
                
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
        pass

    def __getitem__(self, index):
        return self.array[index]
    
    def __setitem__(self, index, value):
        self.array[index] = value