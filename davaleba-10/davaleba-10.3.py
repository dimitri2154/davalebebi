from functools import partial

def is_positive(x):
    return x > 0

numbers = [-8, -5, 0, 5, 10, 15, -3, 8, -1, 2, 9, 12, -15,]

positive_filter = partial(filter, is_positive)

positive_numbers = list(positive_filter(numbers))

print(positive_numbers)