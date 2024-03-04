import random
from cllas import if_else

array = [[random.randint(10, 99) for i in range(5)] for j in range(5)]
sum_list = 0
len_array = 0

for list in array:
    len_array += len(list)
    sum_list += sum(list)
    metrics = [str(j) for j in list]
    print(" ".join(metrics))

average_arithmetic = sum_list / len_array

print()
for list in array:
    lists = if_else(list, average_arithmetic)
    print(" ".join(lists.average))
