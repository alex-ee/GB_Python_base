import re

with open('t123ww','w') as w:
    w.write('1 2 3 4 5 6 7 8 8 9 2 12 33 5 67 89')

with open('t123ww','r') as f:
    i_lines = f.read()

sums = list(map(int, re.findall('\d+', i_lines)))

print(f'сумма {sum(sums)}')
