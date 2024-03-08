from classes import Matrix
from helpers import sep
import random
import helpers

array = [[random.randint(10, 99) for i in range(5)] for j in range(5)]

for list in array:
    print("\U0001f606".join([str(j) for j in list]))

sep()

for child_list in array:
    print("  ".join([str(num) if str(num).__contains__("5") else "  " for num in child_list]))

metrics = Matrix(array)
sep()
metrics.print_values_by_content("5")
