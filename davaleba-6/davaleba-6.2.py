num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter a mathematical operator (+, -, *, /): ")

operations = {
    '+': num1 + num2,
    '-': num1 - num2,
    '*': num1 * num2,
    '/': num1 / num2
    if num2 != 0
    else "შეცდომაა ნულზე გაყოფა!"
}

if operator in operations:
    result = operations[operator]
    print(f"The result of {num1} {operator} {num2} = {result}")
else:
    print("გამოიყენეთ მხოლოდ შემდეგი ოპერატორები +, -, *, /.")
