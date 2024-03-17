from enum import Enum
from uagents import Model

class Guys(str, Enum):
    BAD_GUY = 2
    GOOD_GUY = 1
    EMPTY_SPACE = 0

class NeedHelp(Model):
    coordinates : tuple

class Initialization(Model):
    pass

# matrix = [
#     [1, 0, 0, 1],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [1, 0, 0, 1]
# ]

def read_matrix_from_file(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = [int(num) for num in line.split()]
            matrix.append(row)
    return matrix

matrix = read_matrix_from_file("matrix.txt")