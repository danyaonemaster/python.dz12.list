import random

array = [[random.randint(10, 99) for i in range(5)] for j in range(5)]

for list in range(len(array)):
    metrics = [str(j) for j in array[list]]
    print(" ".join(metrics))

print()
for list in range(len(array)):
    line = ""
    for j in array[list]:
        if str(j)[0] == "5" or str(j)[1] == "5":
            line += f"{j} "
        else:
            line += "   "
    print(line)
