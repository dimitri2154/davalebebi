num1 = float(input("ჩაწერე პირველი რიცხვი: "))
num2 = float(input("ჩაწერე მეორე რიცხვი: "))
operator = input ("ჩაწერე მათემატიკური ოპერატორი (მიმატება +, გამოკლება -, გამრავლება *, გაყოფა /, ახარისხება **, ნაშთი %): ")
if '+' in operator:
    print (num1 + num2)
elif '-' in operator:
    print (num1 - num2)
elif "*" in operator:
    print (num1 * num2)
elif '/' in operator:
    if num2 == 0:
        print("ნულზე არ იყოფა")
    else:
        print (num1 / num2)
elif "**" in operator:
    print (num1 ** num2)

elif "%" in operator:
    print (num1 % num2)
else:
    print ("მათემატიკური ოპერატორი არ მოიძებნა. მხოლოდ შემოთავაზებული მათემატიკური ოპერატორები გამოიყენეთ")