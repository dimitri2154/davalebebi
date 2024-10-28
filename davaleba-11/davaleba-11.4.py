def find_palindrome_pairs(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        palindrome_pairs = []

        for i in range(len(lines)):
            for j in range(i + 1, len(lines)):
                if lines[i] == lines[j][::-1]:
                    palindrome_pairs.append((lines[i], lines[j]))

        if palindrome_pairs:
            print("Palindrome pairs found:")
            for pair in palindrome_pairs:
                print(f'"{pair[0]}" and "{pair[1]}"')
        else:
            print("No palindrome pairs found.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")


file_path = r'C:\Users\dimitri\Documents\step\lesson11\davaleba-11\file1.txt'
find_palindrome_pairs(file_path)
