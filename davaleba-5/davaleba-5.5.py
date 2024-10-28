matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        result[column][row] = matrix[row][column]

for row in result:
    print(row)