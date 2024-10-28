import random

matrix = [[random.randint(1, 100) for _ in range(4)] for _ in range(4)]

for row in matrix:
    print(row)