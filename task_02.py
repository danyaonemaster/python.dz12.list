import random

array = [[random.randint(10, 99) for i in range(5)] for j in range(5)]
sum_list = 0
len_array = 0

for list in range(len(array)):
    metrics = [str(j) for j in array[list]]
    print(" ".join(metrics))

for i in array:
    len_array += len(i)
    sum_list += sum(i)
average_arithmetic = sum_list / len_array

print()
for list in range(len(array)):
    lists = []
    for j in array[list]:
        if j > average_arithmetic:
            lists.append(str(j))
        else:
            lists.append("  ")
    print(" ".join(lists))
