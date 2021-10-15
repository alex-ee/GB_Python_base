import re


sdict = {'1':'один', '2':'два', '3':'три', '4':'четыре'}

with open('t123','r') as f:
    with open('t123w','w') as w:
        for line in f:
            w.write(sdict[re.findall('\d+', line)[0]])
            w.write(' - ')
            w.write(re.findall('\d+', line)[0])
            w.write('\n')
