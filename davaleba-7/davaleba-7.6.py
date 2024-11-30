set1 = {1, 2}
set2 = {'a', 'b'}

result_set = {(x, y) for x in set1 for y in set2}

print("Output:", result_set)
