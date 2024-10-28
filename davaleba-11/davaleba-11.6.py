def remove_empty_lines(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            non_empty_lines = [line for line in infile if line != '\n' and line != '']

        with open(output_file, 'w') as outfile:
            outfile.writelines(non_empty_lines)

        print(f"Empty lines removed. Content written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")

input_file = r'C:\Users\dimitri\Documents\step\lesson11\davaleba-11\input.txt'
output_file = r'C:\Users\dimitri\Documents\step\lesson11\davaleba-11\output.txt'
remove_empty_lines(input_file, output_file)
