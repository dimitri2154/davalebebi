from collections import Counter

def anagram(str1, str2):
    if Counter(str1) == Counter(str2):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")

anagram(input_str1, input_str2)
