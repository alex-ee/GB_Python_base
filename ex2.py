src_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_lsit = []

prev_el = src_list[0]
for el in src_list:
    if el > prev_el:
        new_lsit.append(el)
        
    prev_el = el

print(new_lsit)
