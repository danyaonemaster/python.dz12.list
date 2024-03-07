import random

import helpers
from classes import Matrix

array = [[random.randint(10, 99) for i in range(5)] for j in range(5)]
sum_list = 0
len_array = 0

for list in array:
    len_array += len(list)
    sum_list += sum(list)

average_arithmetic = sum_list / len_array
matrix_average = Matrix(array, average_arithmetic)

matrix_average.print_matrix()
helpers.sep()
matrix_average.get_average()
