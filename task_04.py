import random

import helpers
from classes import Matrix

array = [[random.randint(10, 99) for i in range(5)] for j in range(5)]
list_sum = 0
matrix_even_sum = Matrix(array)

matrix_even_sum.print_matrix()
helpers.sep()

for child_list in array:
    print("  ".join([str(num) if sum(map(int, str(num))) % 2 == 0 else "  "
                     for num in child_list]))

helpers.sep()
matrix_even_sum.get_even_sum()
