import random

kveda_zgvari = int(input("შეიყვანეთ ინტერვალის ქვედა ზღვარი: "))
zeda_zgvari = int(input("შეიყვანეთ ინტერვალის ზედა ზღვარი: "))

secret_number = random.randint(kveda_zgvari, zeda_zgvari)

lives = 5

while lives > 0:
    guess = int(input("გამოიცანით რიცხვი: "))

    if guess == secret_number:
        print("გილოცავთ! თქვენ გამოიცანით რიცხვი!")
        break
    elif guess > secret_number:
        print("თქვენ მიერ შეყვანილი რიცხვი გამოსაცნობ რიცხვზე მაღალია. კიდევ სცადეთ.")
    else:
        print("თქვენ მიერ შეყვანილი რიცხვი გამოსაცნობ რიცხვზე დაბალია. კიდევ სცადეთ.")

    lives -= 1

else:
    print("სიცოცხლე ამოიწურა! სწორი პასუხია:", secret_number)