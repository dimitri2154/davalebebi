import random

random_numbers = [random.randint(1, 1000) for _ in range(20)]
print("List of 20 random numbers:", random_numbers)

odd_numbers = []
for number in random_numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

print("Odd numbers list:", odd_numbers)

if odd_numbers:
    smallest = odd_numbers[0]
    largest = odd_numbers[0]
    for number in odd_numbers:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

    print("Smallest odd number:", smallest)
    print("Largest odd number:", largest)
else:
    print("Not found")