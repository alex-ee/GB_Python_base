
def ex1():
    t = 11
    s = 'sss'

    print(t,s)

    s = input('введите строку: ')

    print(s)
    
def ex2():
    s = input('введите секунды: ')
    
    if str.isdigit(s):
        sec = int(s) % 60
        m = int(s) // 60 % 60
        h = int(s) // 60 // 60 % 24
        
        h = ('0' + str(h))[-2:]
        m = ('0' + str(m))[-2:]
        s = ('0' + str(sec))[-2:]
        
        print(f'{h}:{m}:{s}')

    else:
        print('введено неверное значение')
    
def ex3():
    s = input('введите число: ')
    
    if str.isdigit(s):
        sum = int(s) + int(s+s) + int(s+s+s)
        
        print(sum)

    else:
        print('введено неверное значение')
    
def ex4():
    s = input('введите число: ')
    
    if str.isdigit(s):
        max = int(s[0])
        i = 1
        while i <= len(s) - 1:
            max = int(s[i]) if int(s[i]) > max else max
            i += 1
        
        print(max)

    else:
        print('введено неверное значение')
    
def ex5():
    s = input('введите прибыль: ')
    d = input('введите издержки: ')
    
    if str.isdigit(s) and str.isdigit(d):
        if s > d:
            z = int(s) - int(d)
            
            q = input('в плюсе. введите число сотрудников для распределения выручки: ')
            if str.isdigit(q):
                print(f'по {z/int(q)} на каждого сотрудника')
                
            else:
                print('введено неверное значение')
        
        elif s < d:
            print('отработали в убыток')
        
        else:
            print('отработали в ноль, по 0 на каждого сотрудника')
        
    else:
        print('введено неверное значение')
    
def ex6():
    a = input('введите параметр а: ')
    b = input('введите параметр b: ')
    
    if str.isdigit(a) and str.isdigit(b):
        count = 1
        f = int(a)
        while f < int(b):
            f = f * 1.1
            count += 1
            
        print(f'на {count} день результат составил {f} км')
            
        
    else:
        print('введено неверное значение')


if __name__ == '__main__':
    while True:
        ex_to_run = input('Какое задание будем проверять? (введите номер задачи): ')
        if ex_to_run == '1':
            ex1()
            
        elif ex_to_run == '2':
            ex2()
            
        elif ex_to_run == '3':
            ex3()
            
        elif ex_to_run == '4':
            ex4()
            
        elif ex_to_run == '5':
            ex5()
            
        elif ex_to_run == '6':
            ex6()

        else:
            print('нет такой')