import random


def examination(num):
    return str(num) if str(num).__contains__("5") else "  "


array = [[random.randint(10, 99) for i in range(5)] for j in range(5)]

for list in range(len(array)):
    metrics = [str(j) for j in array[list]]
    print("\U0001f606".join(metrics))

print()
for list in array:
    lists = [examination(num) for num in list]

    print(" ".join(lists))
