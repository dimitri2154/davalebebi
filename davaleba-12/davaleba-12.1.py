import csv

with open('titanic.csv', 'r') as csvfile, open('survived.csv', 'w', newline='') as outfile:
    reader = csv.DictReader(csvfile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        if row['Survived'] == '1' or row['Survived'] == 1:
            writer.writerow(row)