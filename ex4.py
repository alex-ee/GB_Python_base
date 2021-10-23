class StoreTech:
    def __init__(self, name, vol):
        self.name = name
        self.vol = vol
        self.free_vol = vol
        self.stored = {}
        
    def load(self, other):
        if self.free_vol - other.vol <= 0:
            print('Данный товар не поместится на склад')
            return False
        
        try:
            self.stored[other.name] += 1
        except:
            self.stored[other.name] = 1
            
        self.free_vol -= other.vol
        
    def unload(self, other):
        try:
            if self.stored[other.name] <= 0:
                print('Данного товара нет на складе')
                return False
        except:
            print('Данного товара нет на складе')
            return False
        
        self.stored[other.name] -= 1
        self.free_vol += other.vol
        
class Tech:
    def __init__(self, name, vol):
        self.name = name
        self.vol = vol
        
class Printer(Tech):
    def __init__(self,vol):
        super().__init__('Printer',vol)
        
class Scaner(Tech):
    def __init__(self,vol):
        super().__init__('Scaner',vol)
        
