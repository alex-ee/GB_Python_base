class Car:
    def __init__(self, color, name, is_police = False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = 'fwd'
        
        
    def go(self, speed):
        self.speed = speed
        print(f'{self.name} набрала скорость {self.speed}')


    def stop(self):
        self.speed = 0
        print(f'{self.name} остановилась')


    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} повернула {self.direction}')
        self.direction = 'fwd'


    def show_speed(self):
        print(f'Скорость {self.name} {self.speed}')
        

class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)


    def show_speed(self):
        print('превышение скорости!') if self.speed > 60 else 0
        super().show_speed()


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        
    
    def show_speed(self):
        print('превышение скорости!') if self.speed > 40 else 0
        super().show_speed()


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)


t_car = TownCar(
    'red',
    't_car'
)

s_car = SportCar(
    'yellow',
    's_car'
)

w_car = WorkCar(
    'black',
    'w_car'
)

p_car = PoliceCar(
    'blue',
    'p_car'
)


t_car.go(100)
t_car.turn('влево')
t_car.show_speed()
t_car.stop()
t_car.show_speed()

print('====================')

t_car.go(60)
t_car.turn('влево')
t_car.show_speed()
t_car.stop()
t_car.show_speed()

print('====================')

s_car.go(100)
s_car.turn('влево')
s_car.show_speed()
s_car.stop()
s_car.show_speed()

print('====================')

w_car.go(100)
w_car.turn('влево')
w_car.show_speed()
w_car.stop()
w_car.show_speed()

print('====================')

w_car.go(40)
w_car.turn('влево')
w_car.show_speed()
w_car.stop()
w_car.show_speed()

print('====================')

p_car.go(100)
p_car.turn('влево')
p_car.show_speed()
p_car.stop()
p_car.show_speed()