class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}
        
        
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)


    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._Worker__income["wage"] + self._Worker__income["bonus"]


pos = Position(
    'Name',
    'SurName',
    'Pos',
    1000,
    100
)

print(pos.get_full_name())

print(pos.get_total_income())
