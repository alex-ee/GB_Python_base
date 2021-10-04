my_list = [7, 5, 3, 3, 2]

i = input('Введите число: ')

if i.isdigit:
    i = int(i)
    
    if i >= my_list[0]:
            my_list = [i] + my_list
            
    elif i <= my_list[-1]:
        my_list = my_list + [i]
        
    else:
        if abs(my_list[0] - i) > abs(my_list[-1] - i):
            z = len(my_list)-1
            while i > my_list[z]:
                z -= 1
            z += 1
            
        else:
            z = 0
            while i < my_list[z]:
                z += 1

        my_list = my_list[:z] + [i] + my_list[z:]
        
    print(my_list)
    
else:
    print('Введено не число')
