import random


def comparison(num: str):
    sum = 0
    for index in range(len(num)):
        sum += int(num[index])
    return num if sum % 2 == 0 else "  "


array = [[random.randint(10, 99) for i in range(5)] for j in range(5)]

for index in range(len(array)):
    metrics = [str(j) for j in array[index]]
    print(" ".join(metrics))

print()
for list in array:
    lists = [comparison(str(num)) for num in list]
    print(" ".join(lists))
