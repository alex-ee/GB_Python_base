import re
import typing


list = [1,2,'3',4,'5',{6},[7]]

for i in list:
    print(f'\n{i}\t{type(i)}')
    print(f'{i}\tэто int?\t{isinstance(i, int)}')
    print(f'{i}\tэто List?\t{isinstance(i, typing.List)}')
    print(f'{i}\tэто str?\t{isinstance(i, str)}')
    print(f'{i}\tэто хэш?\t{isinstance(i, set)}')
    