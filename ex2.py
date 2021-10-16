class Road:
    kgs_per_sqm = 25
    
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        print(f'Создана дорога \t{self.__length}x{self.__width}')
    
    
    def calc_w_in_kgs(self, i_th):
        return self.__length * self.__width * self.kgs_per_sqm * i_th

rd = Road(20, 5000)

print(rd.calc_w_in_kgs(5))