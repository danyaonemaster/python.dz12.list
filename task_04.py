import random
from cllas import if_else


array = [[random.randint(10, 99) for i in range(5)] for j in range(5)]
list_sum = 0
for index in range(len(array)):
    metrics = [str(j) for j in array[index]]
    print(" ".join(metrics))

print()
for list in array:
    output_sum_even = if_else(list)
    print(" ".join(output_sum_even.even))
