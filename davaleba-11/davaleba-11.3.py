file1_path = 'file1.txt'
file2_path = 'file2.txt'
merged_file_path = 'merged_file.txt'

with open(file1_path, 'w') as file1:
    file1.write("Fusce orci felis, porttitor vel convallis quis, consequat sodales libero.\n"
                "Duis urna nunc, molestie vitae porta sed, aliquam eu felis.\n"
                "Praesent in est at lorem viverra tincidunt. Nunc mollis feugiat ex id dignissim.\n"
                "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.\n"
                "Mauris aliquam finibus magna vel commodo. Donec volutpat volutpat mollis.\n"
                "Vestibulum malesuada faucibus interdum. Donec nec tempus tortor.\n"
                "Etiam semper est quis diam sodales auctor. Nullam vel sapien in tellus interdum commodo sit amet ut arcu.\n"
                "Vivamus tortor leo, viverra quis auctor et, finibus sed ex. Donec tellus ex, rhoncus quis pretium in, porttitor nec sem.")

with open(file2_path, 'w') as file2:
    file2.write("Ut vulputate ex turpis, gravida vehicula turpis sollicitudin eu.\n"
                "In a libero dolor. Nam condimentum quam sit amet interdum ullamcorper.\n"
                "Fusce semper est vel risus egestas ultricies. Sed sed iaculis metus.\n"
                "Aenean scelerisque tristique facilisis. Integer hendrerit ligula vitae dolor ultrices aliquam.")

with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(merged_file_path, 'w') as merged_file:
    merged_file.write(file1.read())
    merged_file.write(file2.read())

with open(merged_file_path, 'r') as merged_file:
    combined_content = merged_file.read()
    print("Combined File Content:")
    print(combined_content)
