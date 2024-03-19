from enum import Enum
from uagents import Agent, Model

class Guys(str, Enum):
    BAD_GUY = 2
    GOOD_GUY = 1
    EMPTY_SPACE = 0

class NeedHelp(Model):
    coordinates : tuple

class StopSearching(Model):
    pass

def read_matrix_from_file(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = [int(num) for num in line.split()]
            matrix.append(row)
    return matrix

matrix = read_matrix_from_file("matrix.txt")
rows = len(matrix)
cols = len(matrix[0])

police_agent = Agent(name="police", seed="police")
radar_upleft = Agent(name="radar_upleft", seed="radar_upleft recovery phrase")
radar_upright = Agent(name="radar_upright", seed="radar_upright recovery phrase")
radar_bottomleft = Agent(name="radar_bottomleft", seed="radar_bottomleft recovery phrase")
radar_bottomright = Agent(name="radar_bottomright", seed="radar_bottomright recovery phrase")

def init_all():
    radar_upleft._storage.set("i", 0)
    radar_upleft._storage.set("j", 0)
    radar_upleft._storage.set("i_start", 0)
    radar_upleft._storage.set("j_start", 0)
    radar_upleft._storage.set("i_end", int(rows/2))
    radar_upleft._storage.set("j_end", int(cols/2))
    radar_upleft._storage.set("moving", True)

    radar_upright._storage.set("i", int(rows/2))
    radar_upright._storage.set("j", int(cols/2))
    radar_upright._storage.set("i_start", int(rows/2))
    radar_upright._storage.set("j_start", int(cols/2))
    radar_upright._storage.set("i_end", rows)
    radar_upright._storage.set("j_end", cols)
    radar_upright._storage.set("moving", True)

    radar_bottomleft._storage.set("i", int(rows/2))
    radar_bottomleft._storage.set("j", 0)
    radar_bottomleft._storage.set("i_start", int(rows/2))
    radar_bottomleft._storage.set("j_start", 0)
    radar_bottomleft._storage.set("i_end", rows)
    radar_bottomleft._storage.set("j_end", int(cols/2))
    radar_bottomleft._storage.set("moving", True)

    radar_bottomright._storage.set("i", int(rows/2))
    radar_bottomright._storage.set("j", int(cols/2))
    radar_bottomright._storage.set("i_start", int(rows/2))
    radar_bottomright._storage.set("j_start", int(cols/2))
    radar_bottomright._storage.set("i_end", rows)
    radar_bottomright._storage.set("j_end", cols)
    radar_bottomright._storage.set("moving", True)