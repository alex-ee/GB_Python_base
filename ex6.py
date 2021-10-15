import re

sdict = {}
with open('program.txt','r') as f:
    for line in f:
        sdict[re.findall('[а-яА-Я]+:', line)[0]] = sum(list(map(int, re.findall('\d+', line))))

print(sdict)