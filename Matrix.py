class Matrix:
    def __init__(self, array):
        self.array = array

    def __repr__(self):
        pass

    def __iter__(self):
        pass

    def __getitem__(self, index):
        return self.array[index]
    
    def __setitem__(self, index, value):
        self.array[index] = value