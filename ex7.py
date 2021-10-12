from functools import reduce


def fact(n):
    new_list = []
    for i in range(1,n+1): new_list.append(i)
    
    yield reduce(lambda x, y: x * y, new_list)


if __name__ == '__main__':
    for el in fact(4):
        print(el)
