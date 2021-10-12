from functools import reduce


new_list = []
for i in range(100,1001): new_list.append(i) if i%2 == 0 else 1

print(reduce(lambda x, y: x * y, new_list))