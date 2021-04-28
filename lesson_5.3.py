list_num = [50,40,1,23,56,67,21,67,896,32,12,44,11]
more_then = [list_num[num] for num in range(1, len(list_num)) if list_num[num] > list_num[num - 1]]

print(more_then)