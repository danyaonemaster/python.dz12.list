from cllas import Matrix
import random

array = [[chr(random.randint(65, 90)) for i in range(5)] for j in range(5)]
matrix_letter = Matrix(array)

matrix_letter.get_matrix()
print()
matrix_letter.get_letters()