import random

array = [[chr(random.randint(65, 90)) for i in range(5)] for j in range(5)]

for list in range(len(array)):
    metrics = [str(j) for j in array[list]]
    print(" ".join(metrics))

print()
for list in array:
    lists = [letter if letter == "T" else " "
             for letter in list]

    print(" ".join(lists))
