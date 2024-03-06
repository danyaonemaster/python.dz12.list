class Matrix:
    def __init__(self, array, arith_averag=0):
        self.array = array
        self.arith_averag = arith_averag

    def get_matrix(self):
        for list in self.array:
            print("  ".join([str(num) for num in list]))

    def get_values(self):
        for list in self.array:
            print("  ".join([str(num) if str(num).__contains__("5") else "  "
                             for num in list]))

    def get_letters(self):
        for list in self.array:
            print("  ".join([letter if letter == "T" else " "
                             for letter in list]))

    def get_average(self):
        for list in self.array:
            print("  ".join([str(num) if num > self.arith_averag
                             else "  " for num in list]))

    def get_even_sum(self):
        for list in self.array:
            print("  ".join([str(num) if sum(map(int, str(num))) % 2 == 0 else "  "
                             for num in list]))
