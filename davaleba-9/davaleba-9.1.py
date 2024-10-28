int_list = [10, 20, 30, 40]

def add_to_list(number):

  global int_list
  int_list.append(number)

number = int(input("Enter a number: "))

add_to_list(number)
print(f"Updated list: {int_list}")