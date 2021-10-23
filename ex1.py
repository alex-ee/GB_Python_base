class WrongDateFormat(Exception):
    pass

class Дата:
    def __init__(self, s_date):
        if not Дата.check_date(s_date):
            raise WrongDateFormat
        
        self.day, self.month, self.year = Дата.to_int(s_date)
        
    @classmethod
    def to_int(cls, s_date):
        return map(int, s_date.split('-'))
    
    @staticmethod
    def check_date(s_date):
        day, month, year = Дата.to_int(s_date)
        return True if day in range(1, 32) and month in range(1,13) and year in range(1900, 3999) else False
        
        
        
m = Дата('11-12-2020')

