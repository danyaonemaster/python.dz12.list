class if_else:
    def __init__(self, list, average=0):
        self.letters = [letter if letter == "T" else " "
                        for letter in list]

        self.values = [str(num) if str(num).__contains__("5") else "  "
                       for num in list]

        self.average = [[str(num) if num < average
                         else "  " for num in list]]
