def fibonachi_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]

    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)

    return fib_sequence

n = int(input("შეიყვანეთ ფიბონაჩის მიმდევრობის წევრთა რაოდენობა: "))
print(fibonachi_sequence(n))