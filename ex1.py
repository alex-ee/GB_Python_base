import time
from itertools import cycle


class TrafficLight:
    dict_colors = {'red': 7, 'yellow': 2, 'green': 5}
    
    
    def __next_color__(self):
        for el in cycle(self.dict_colors):
            yield el

        
    def __init__(self):
        self.__sem_gen = self.__next_color__()
        self._color = next(self.__sem_gen)
        print(f'Загорелся\t{self._color}\tсвет')
        
    
    def running(self):
        time.sleep(self.dict_colors[self._color])
        self._color = next(self.__sem_gen)
        print(f'Загорелся\t{self._color}\tсвет')


sem = TrafficLight()

i_count = 0
while i_count < 8:
    sem.running()
    i_count += 1