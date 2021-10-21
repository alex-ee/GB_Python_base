from abc import ABC, abstractmethod

class Closer:
    def __init__(self, name, util):
        self.name = name
        self.util_z = util

    @property
    @abstractmethod
    def util(self):
        return self.util_z
    
    @abstractmethod
    def __add__(self, other):
        return self.util_z + other.util_z
        
        
class Coat(Closer):
    def __init__(self, size):
        self.size = size
        super().__init__('Coat', size/6.5 + .5)


class Costume(Closer):
    def __init__(self, grows):
        self.grows = grows
        super().__init__('Costume', grows*2 + .3)

    
c1 = Coat(23)
c2 = Costume(22)

print(c1.util)
print(c2.util)

print(c1 + c2)