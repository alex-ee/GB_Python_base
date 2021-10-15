t_str = '1'
with open('test.txt', 'w') as f:
    while t_str:
        t_str = input('введите что-ниб: ')
        f.write(f'{t_str}\n')
