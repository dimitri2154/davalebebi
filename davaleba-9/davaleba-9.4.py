def fibonacci(n):

  if n <= 0:
    return []
  elif n == 1:
    return [0]
  elif n == 2:
    return [0, 1]
  else:
    fibonacci_sequence = fibonacci(n - 1)
    next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_fibonacci)
    return fibonacci_sequence


num_terms = int(input("შეიყვანეთ ფიბონაჩის მიმდევრობის წევრთა რაოდენობა: "))

fibonacci_sequence = fibonacci(num_terms)
print(f"ფიბონაჩის მიმდევრობაა: {fibonacci_sequence}")