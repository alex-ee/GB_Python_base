import re 

class Complex:
    def __init__(self, s_data):
        # self.operation = re.findall('\-|\+', s_data)[0]
        self.operation = '+'
        s_int, s_jint = s_data.split(self.operation)
        self.int = int(s_int)
        self.jint = [int(re.findall('[0-9]+', s_jint)[0]), re.findall('[a-zA-Z]+', s_jint)[0]]

    def __add__(self, other):
        # return Complex(f'{self.int + other.int}{self.operation if self.jint[0] >= other.jint[0] else other.operation}{self.jint[0] - other.jint[0] if self.jint[0] >= other.jint[0] else other.jint[0] - self.jint[0]}{self.jint[1]}')
        return Complex(f'{self.int + other.int}{self.operation}{self.jint[0] + other.jint[0]}{self.jint[1]}')
        
    def __mul__(self, other):
        # if self.operation == '-' or other.operation == '-':
        #     res_operation = '-'
            
        # else:
        #     res_operation = '+'

        cpx1 = Complex(
            f'{self.int * other.int}{self.operation}{self.int * other.jint[0]}{other.jint[1]}'
        ) + Complex(
            f'0{self.operation}{self.jint[0] * other.int}{self.jint[1]}'
        )
        
        cpx1.int -= self.jint[0] * other.jint[0]
        
        # if res_operation == '+':
        #     cpx1.int -= self.jint[0] * other.jint[0]
            
        # else:
        #     cpx1.int += self.jint[0] * other.jint[0]
            
        return cpx1
    
    def __str__(self):
        return f'{self.int}{self.operation}{self.jint[0]}{self.jint[1]}'
        

a1 = Complex('6+7j')
a2 = Complex('4+9j')

print(a1)
print(a2)

print(a1 + a2)

print(a1 * a2)
