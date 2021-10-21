class WrongCounters(Exception):
    pass

class Cell:
    def __init__(self, count_cells):
        self.count_cells = count_cells
        
    def __add__(self, other):
        return Cell(self.count_cells + other.count_cells)
    
    def __sub__(self, other):
        return Cell(self.count_cells - other.count_cells) if self.count_cells - other.count_cells > 0 else WrongCounters
    
    def __mul__(self, other):
        return Cell(self.count_cells * other.count_cells)
    
    def __truediv__(self, other):
        return Cell(round(self.count_cells / other.count_cells))
    
    def __str__(self):
        return str(self.count_cells)
    
    def make_order(self, cpr):
        rows = self.count_cells // cpr
        st = ''
        for i in range(0, rows):
            st += cpr*'*' + '\\n'
        
        st += self.count_cells % cpr * '*'
        
        return st
            

m1 = Cell(20)
m2 = Cell(30)

print(m2 + m1)
print(m2 - m1)
print(m2 * m1)
print(m2 / m1)

print(m1.make_order(8))
