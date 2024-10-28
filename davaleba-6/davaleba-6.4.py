departments = {
    "Sales": [
        {"first_name": "Giorgi", "last_name": "Giorgadze", "age": 30, "salary": 6000},
        {"first_name": "Natia", "last_name": "Beridze", "age": 39, "salary": 5500},
    ],
    "Marketing": [
        {"first_name": "Gvantsa", "last_name": "Kiladze", "age": 35, "salary": 7000},
        {"first_name": "Lasha", "last_name": "Bakradze", "age": 28, "salary": 6500},
    ],
    "HR": [
        {"first_name": "Maia", "last_name": "Kiknadze", "age": 38, "salary": 8000},
        {"first_name": "Keti", "last_name": "Benidze", "age": 35, "salary": 7500},
    ],
    "PR": [
        {"first_name": "Inga", "last_name": "Elisashvili", "age": 36, "salary": 8000},
        {"first_name": "Diana", "last_name": "Gorgodze", "age": 27, "salary": 6000},
    ],
}

for department, employees in departments.items():
    total_salary = sum(employee["salary"] for employee in employees)
    average_salary = total_salary / len(employees)
    print(f"Average salary in {department}: {average_salary}")
