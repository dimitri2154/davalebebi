numbers = {
    2: "two",
    8: "eight",
    10: "ten",
    13: "thirteen",
    17: "seventeen"
}

with open("numbers.txt", "w") as f:
    for i in range(1, 18):
        if i in numbers:
            f.write(f"Line {i}: {numbers[i]}\n")
        else:
            f.write(f"Line {i}\n")

            