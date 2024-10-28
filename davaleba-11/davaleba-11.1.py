
with open("my_file.txt", "w") as f:
    for i in range(1, 1001):
        f.write(f"This is line {i}.\n")

with open("my_file.txt", "r") as f:
    lines = f.readlines()
    num_lines = len(lines)

print(f"The file has {num_lines} lines.")