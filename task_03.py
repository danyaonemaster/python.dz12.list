import random

array = [[chr(random.randint(65, 90)) for i in range(5)] for j in range(5)]

for list in range(len(array)):
    metrics = [str(j) for j in array[list]]
    print(" ".join(metrics))

print()
for list in range(len(array)):
    lists = []
    for j in array[list]:
        if j == "T":
            lists.append(j)
        else:
            lists.append("  ")
    print(" ".join(lists))
