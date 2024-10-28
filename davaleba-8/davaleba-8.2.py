def count_character(string, character):
    return string.count(character)

user_string = input("Enter a string: ")
user_character = input("Enter a character: ")

if len(user_character) != 1:
    print("მხოლოდ 1 სიმბოლო შეიყვანეთ.")
else:
    result = count_character(user_string, user_character)
    print(f"შეყვანილ ტექსტში სიმბოლო '{user_character}' {result}-ჯერ გვხვდება.")
