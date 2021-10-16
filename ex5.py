class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')
        

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)


    def draw(self):
        super().draw()
        print(f'отрисовка {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)


    def draw(self):
        super().draw()
        print(f'отрисовка {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)


    def draw(self):
        super().draw()
        print(f'отрисовка {self.title}')


s_pen = Pen('ручкой')

s_pcl = Pencil('карандашом')

s_hdl = Handle('маркером')


s_pen.draw()

s_pcl.draw()

s_hdl.draw()