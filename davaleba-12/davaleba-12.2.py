import csv

with open('organizations-100.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

data.sort(key=lambda row: int(row['Number of employees']))

with open('sorted_csv.csv', 'w', newline='') as sorted_csv_file:
    fieldnames = data[0].keys()
    csv_writer = csv.DictWriter(sorted_csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(data)

print("File created: sorted_csv.csv")