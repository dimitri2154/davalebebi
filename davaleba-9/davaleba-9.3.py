def reverse_string(text):

  if len(text) <= 1:
    return text
  else:
    return reverse_string(text[1:]) + text[0]

string = input("Enter a string: ")

reversed_string = reverse_string(string)
print(f"The reversed string is: {reversed_string}")