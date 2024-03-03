import random

def examination(num, aver_arith):
    return str(num) if num < aver_arith else "  "


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
for list in array:
    lists = [ examination(num,average_arithmetic) for num in list]
    print(" ".join(lists))
