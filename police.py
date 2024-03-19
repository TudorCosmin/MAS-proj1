from uagents import Context
from environment import Guys
from environment import NeedHelp
from environment import matrix
from environment import police_agent

def lee_algorithm(input_coord, target_coord, matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    distance = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    
    queue = [input_coord]
    visited = set()
    visited.add(input_coord)
    
    # Define possible moves: up, down, left, right
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        current = queue.pop(0)
        if current == target_coord:
            return distance[current[0]][current[1]]
        
        for move in moves:
            new_row = current[0] + move[0]
            new_col = current[1] + move[1]
            
            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] != 1 and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))
                distance[new_row][new_col] = distance[current[0]][current[1]] + 1
    
    return -1

@police_agent.on_message(model=NeedHelp, replies=set())
async def give_help(ctx: Context, sender: str, msg: NeedHelp):
    index = 0
    for i in range(100000000):
        index = index + 1

    coord = msg.coordinates
    matrix[coord[0]][coord[1]] = Guys.EMPTY_SPACE
    
    ctx.logger.info("police done for looking for bad guys")

# def count_clusters(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     matrix_copy = [row[:] for row in matrix]  # Create a deep copy of the matrix
    
#     def fill(row, col):
#         if row < 0 or row >= rows or col < 0 or col >= cols or matrix_copy[row][col] != 0:
#             return
#         matrix_copy[row][col] = -1  # Mark as visited
#         fill(row + 1, col)           # Fill down
#         fill(row - 1, col)           # Fill up
#         fill(row, col + 1)           # Fill right
#         fill(row, col - 1)           # Fill left
    
#     cluster_count = 0
#     for i in range(rows):
#         for j in range(cols):
#             if matrix_copy[i][j] == 0:
#                 fill(i, j)
#                 cluster_count += 1
    
#     return cluster_count

# import random
# def transform_random_half(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     num_ones_to_transform = sum(row.count(1) for row in matrix) // 2

#     indices_to_transform = []
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == 1:
#                 indices_to_transform.append((i, j))
    
#     # Randomly shuffle the indices
#     random.shuffle(indices_to_transform)
    
#     # Transform half of the 1s into 0s
#     for idx in indices_to_transform[:num_ones_to_transform]:
#         matrix[idx[0]][idx[1]] = 0
    
#     with open("matrix2.txt", "w") as f:
#         for row in matrix:
#             f.write(' '.join(map(str, row)) + '\n')
#     # print(count_clusters(matrix=matrix))
#     return matrix

# # # Example usage:
# # input_coord = (0, 0)
# # target_coord = (2, 8)
# matrix = environment.read_matrix_from_file("matrix.txt")
# print("no1 init: {}".format(sum(row.count(1) for row in matrix)))
# idx = 0
# while count_clusters(matrix) != 1:
#     matrix = environment.read_matrix_from_file("matrix.txt")
#     matrix = transform_random_half(matrix)
#     idx += 1
# print("no1: {}".format(sum(row.count(1) for row in matrix)))
# print(idx)
# # for line in matrix:
# #     print(line)
# # print(count_clusters(matrix=matrix))
# # print(lee_algorithm(input_coord, target_coord, matrix))  # Output: 4