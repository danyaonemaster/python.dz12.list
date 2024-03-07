class Matrix:
    multy_list = [[]]
    arith_avg = 0

    def __init__(self, multy_list, arith_avg=0):
        self.multy_list = multy_list
        self.arith_avg = arith_avg

    def print_matrix(self):
        for child_list in self.multy_list:
            print("  ".join([str(num) for num in child_list]))

    def print_values_by_content(self, contains: str):
        for child_list in self.multy_list:
            print("  ".join([str(num) if str(num).__contains__(contains) else "  " for num in child_list]))

    def get_letters(self):
        for child_list in self.multy_list:
            print("  ".join([letter if letter == "T" else " "
                             for letter in child_list]))

    def get_average(self):
        for child_list in self.multy_list:
            print("  ".join([str(num) if num > self.arith_avg
                             else "  " for num in child_list]))

    def get_even_sum(self):
        for child_list in self.multy_list:
            print("  ".join([str(num) if sum(map(int, str(num))) % 2 == 0 else "  "
                             for num in child_list]))
