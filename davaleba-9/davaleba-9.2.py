def sum_digits(number):

  if number < 10:
    return number
  else:
    last_digit = number % 10
    remaining_digits = number // 10
    return last_digit + sum_digits(remaining_digits)


num = int(input("Enter a positive integer: "))

result = sum_digits(num)
print(f"შეყვანილი რიცხვის ციფრთა ჯამია: {result}")