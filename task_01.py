import random

array = [[random.randint(10, 99) for i in range(5)] for j in range(5)]

for index in range(len(array)):
    metrics = [str(j) for j in array[index]]
    print("\U0001f606".join(metrics))

print()
for list in array:
    lists = [str(num) if str(num).__contains__("5") else "  "
             for num in list]

    print("\U0001f606".join(lists))
