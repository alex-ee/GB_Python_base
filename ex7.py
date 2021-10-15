import json


sum_prib = 0
count_prib = 0
js = []
sdict = {}
with open('firm.txt','r') as f:
    for line in f:
        sfirm, sform, sviruch, sizderzh = line.split()
        
        prib = int(sviruch) - int(sizderzh)
        
        sum_prib += prib if prib >= 0 else 0
        count_prib += 1 if prib >= 0 else 0
        
        sdict[sfirm] = prib

js.append(sdict)

avg_prib = sum_prib/count_prib

sdict = {}
sdict['average_profit'] = avg_prib

js.append(sdict)

print (js)

with open('firm.json','w') as w:
    json.dump(js, w)