def my_func(arg1, arg2, arg3):
    m = [arg1, arg2, arg3]
    m.sort(reverse = True)
    
    return m[0] + m[1]

print(my_func(2, 1, 6))