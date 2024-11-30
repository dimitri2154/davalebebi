tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (4, 5, 5, 6, 6, 7)

combined_tuple = tuple1 + tuple2
combined_tuple = tuple(set(combined_tuple))

duplicated_values = []
for item in tuple1:
    if item in tuple2 and item not in duplicated_values:
        duplicated_values.append(item)

print("combined_tuple:", combined_tuple)
print("duplicated_values:", duplicated_values)
