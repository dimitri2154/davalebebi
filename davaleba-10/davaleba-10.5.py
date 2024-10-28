from functools import reduce


def product_of_elements():

    user_input = input("Enter a list of numbers separated by spaces: ")

    try:
        numbers = [float(num) for num in user_input.split()]
    except ValueError:
        return "Error: All elements must be numbers."

    return reduce(lambda x, y: x * y, numbers)

result = product_of_elements()
print(result)
