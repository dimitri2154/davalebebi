total_sum = 0

while True:
    user_input = input("მხოლოდ დადებითი რიცხვები შეიყვანეთ! ჯამის გამოსათვლელად დაწერეთ sum: ")

    if user_input == 'sum':
        break

    number = float(user_input)

    if number > 0:
       total_sum += number
    else:
        print("მხოლოდ დადებითი რიცხვები შეიყვანეთ!!!")

print("შეყვანილი დადებითი რიცხვების ჯამია:", total_sum)
