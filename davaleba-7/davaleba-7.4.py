input_tuple = (1, 2, 3, 4)

swapped_tuple = (input_tuple[-1],) + input_tuple[1:-1] + (input_tuple[0],)

print("Output:", swapped_tuple)
