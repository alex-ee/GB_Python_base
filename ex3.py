import re

with open('test.txt','r') as f:
    i_lines = f.read()

sums = list(map(int, re.findall('\d+', i_lines)))

print(f'средняя {sum(sums)/len(sums)}')
