import csv

def find_ssl_companies(input_filename, output_filename):

    ssl_companies = []

    with open(input_filename, 'r', newline='') as infile:
        reader = csv.DictReader(infile)

        for row in reader:
            website = row['Website']
            if website.startswith('https://'):
                ssl_companies.append({
                    'Organization Id': row['Organization Id'],
                    'Name': row['Name'],
                    'Website': row['Website'],
                    'Industry': row['Industry'],
                    'Number of employees': row['Number of employees']
                })

    with open(output_filename, 'w', newline='') as ssl_csv_file:
        fieldnames = ['Organization Id', 'Name', 'Website', 'Industry', 'Number of employees']
        csv_writer = csv.DictWriter(ssl_csv_file, fieldnames=fieldnames)

        csv_writer.writeheader()
        csv_writer.writerows(ssl_companies)

find_ssl_companies('organizations-100.csv', 'ssl_companies.csv')

print("File created: ssl_companies.csv")