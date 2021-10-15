with open('test.txt','r') as f:
    i_lines = f.readlines()

print(f'всего строк: {i_lines.count}')
    
z = 1
for i in i_lines:
    print(f'линия {z}: {len(i.split())} слов')
    z += 1
