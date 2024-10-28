text = input("შეიყვანეთ ტექსტი: ")
words_to_search = ["small", "tall", "middle"]

if 'small' in text:
    print('small')
elif 'tall' in text:
    print('tall')
elif 'middle' in text:
    print('middle')
else:
    print('მოცემული სამი სიტყვა ტექსტში არ მოიძებნა')