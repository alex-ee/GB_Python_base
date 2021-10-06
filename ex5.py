x = 0
while True:
    m = input('введите строку чисел через пробел ("x" для выхода): ').split()
    
    for z in m:
        if z == 'x':
            print(x)
            exit(0)
            
        x += int(z)
    
    print(x)
    