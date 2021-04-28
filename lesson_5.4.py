src = [2,2,2,7,23,1,44,44,3,2,10,7,4,11]
print([i for i in src if src.count(i) == 1])

my_list = {i: 0 for i in src}

for i in src:
    if i in my_list:
        my_list[i] += 1

print([i for i in my_list if my_list[i] == 1])

