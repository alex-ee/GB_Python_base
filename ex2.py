
lst = input('Введите числа через запятую: ')

lst = lst.split(',')
print(f'Введён список: {lst}')

switch_last = len(lst) % 2 == 0

if len(lst) > 1:
    i = 0
    while i <= len(lst)-1:
        if i > 0 and i != len(lst)-1:
            tmp = lst[i-1]
            lst[i-1] = lst[i]
            lst[i] = tmp
            
        elif i == len(lst)-1 and switch_last:
            tmp = lst[i-1]
            lst[i-1] = lst[i]
            lst[i] = tmp
        
        i += 1
    
    print(lst)
    
else:
    print('Введен только один элемент')