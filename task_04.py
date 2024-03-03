import random

array = [[random.randint(10, 99) for i in range(5)] for j in range(5)]

for list in range(len(array)):
    metrics = [str(j) for j in array[list]]
    print(" ".join(metrics))

print()
for list in range(len(array)):
    lists = []
    for j in array[list]:
        number_str = str(j)
        if (int(number_str[0]) + int(number_str[1])) % 2 == 0:
            lists.append(str(j))
        else:
            lists.append("  ")
    print(" ".join(lists))
