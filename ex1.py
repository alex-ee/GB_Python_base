class WrongDimension(Exception):
    pass


class Matrix:
    def __init__(self, mtx_data):
        self.data = mtx_data


    def __str__(self):
        st = ''
        for r in self.data:
            for c in r:
                st += f'{c}\t'
            st += f'\n'
        return st
    

    def __add__(self, other_Matrix):
        s_len = len(self.data)
        a_len = len(other_Matrix.data)
        
        if s_len != a_len:
            raise WrongDimension
        
        new_mtx = []
        for i in range(0,s_len):
            s_r_len = len(self.data[i])
            a_r_len = len(other_Matrix.data[i])
            
            if s_r_len != a_r_len:
                raise WrongDimension
            
            new_row = []
            
            for j in range(0,s_r_len):
                new_row.append(self.data[i][j] + other_Matrix.data[i][j])
                
            new_mtx.append(new_row)
        
        return Matrix(new_mtx)
    
    
m = Matrix([
    [1,2,8],
    [2,3,9],
    [4,5,8],
    [6,7,6]
    ])

m1 = Matrix([
    [1,2,1],
    [2,3,2],
    [4,5,3],
    [6,7,4]
    ])

print(m)
print(m1)

print(m + m1)