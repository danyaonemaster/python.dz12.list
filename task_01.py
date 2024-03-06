from cllas import Matrix
import random

array = [[random.randint(10, 99) for i in range(5)] for j in range(5)]

for list in array:
    print("\U0001f606"
          .join([str(j) for j in list]))

metrics = Matrix(array)

metrics.get_values()
