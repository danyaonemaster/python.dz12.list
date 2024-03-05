from cllas import if_else
import random

array = [[random.randint(65, 90) for i in range(5)] for j in range(5)]

for index in range(len(array)):
    metrics = [str(j) for j in array[index]]
    print(" ".join(metrics))

print()
for list in array:
    lists = if_else(list)
    print(" ".join(lists.letters))
