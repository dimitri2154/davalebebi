
strings = ["level", "hello", "world", "radar", "python", "madam"]

palindromes = list(filter(lambda s: s == s[::-1], strings))

print(palindromes)
