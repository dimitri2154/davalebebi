import re

txt = input("შეიყვანეთ ტექსტი: ")

txt = txt.lower()

txt = re.sub(r'[^a-zA-Z0-9]', '', txt)

if txt == txt[::-1]:
    print("მოცემული ტექსტი პალინდრომია")
else:
    print("მოცემული ტექსტი არ არის პალინდრომი")
