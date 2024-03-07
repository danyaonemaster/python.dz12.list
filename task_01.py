from classes import Matrix
from helpers import sep
import random
import helpers


array = [[random.randint(10, 99) for i in range(5)] for j in range(5)]

for list in array:
    print("\U0001f606".join([str(j) for j in list]))

metrics = Matrix(array)
sep()
metrics.print_values_by_content("5")
