"""
ეს არის სტუდენტების მართვის სისტემა, რომელიც მომხმარებლებს
საშუალებას აძლევს დაამატონ, ნახონ, მოძებნონ და განაახლონ ინფორმაცია სტუდენტების შესახებ.
იგი იყენებს ობიექტზე ორიენტირებულ პროგრამირების პრინციპებს,
მათ შორის მემკვიდრეობას და პოლიმორფიზმს, შეყვანის ვალიდაციას, ახარისხებს სტუდენტის მონაცემებს
და ინახავს მას ავტომატურად CSV ფაილში.

"""

import csv

class Student:
    """
    ეს არის სტუდენტთა კლასი, რომელიც მოიცავს ისეთ ატრიბუტებს,,
    როგორიცაა მათი სახელი, სიის ნომერი, ქულები და ა.შ
    """
    def __init__(self, last_name, first_name, gender, roll_number, program, year_of_study, year_of_enrollment, activity, midterm, final, status="active"):
        """
            last_name (str): სტუდენტის გვარი.
            first_name (str): სტუდენტის სახელი.
            gender (str): სქესი (M/F).
            roll_number (int): სიის ნომერი.
            program (str): სტუდენტის სასწავლო პროგრამა.
            year_of_study (int): სწავლების წელი.
            year_of_enrollment (int): ჩარიცხვის წელი.
            activity (int): აქტიურობის ქულა.
            midterm (int): შუალედურის ქულა.
            final (int): ფინალურის ქულა.
            status (str): სტატუსი (აქტიური, შეწყვეტილი, გარიცხული).
        """
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.roll_number = roll_number
        self.program = program
        self.year_of_study = year_of_study
        self.year_of_enrollment = year_of_enrollment
        self.activity = activity
        self.midterm = midterm
        self.final = final
        self.status = status

    # ობიექტს გარდაქმნის სტრიქონად. გამოიძახება, როდესაც ობიექტი გადაეცემა print() და str() ფუნქციებს.
    def __str__(self):
        return (f"Name: {self.last_name} {self.first_name}, Gender: {self.gender}, "
                f"Roll Number: {self.roll_number}, Program: {self.program}, "
                f"Year: {self.year_of_study}, Enrolled: {self.year_of_enrollment}, "
                f"Activity: {self.activity}, Midterm: {self.midterm}, Final: {self.final}, "
                f"Status: {self.status}")

    # ითვლის საბოლოო ქულას (activity + midterm + final).
    def calculate_total_grade(self):
        return self.activity + self.midterm + self.final

    # საბოლოო ქულის გათვალისწინებით ითვლის GPA-ს, ქვემოთ მოცემული განაწილებით.
    def calculate_gpa(self):
        total_grade = self.calculate_total_grade()
        if total_grade >= 90:
            return 4.0
        elif total_grade >= 80:
            return 3.0
        elif total_grade >= 70:
            return 2.0
        else:
            return 1.0


class BachelorStudent(Student):
    """
    ბაკალავრიატის სტუდენტთა კლასი, მემკვიდრეობით მიღებული სტუდენტური კლასიდან..
    """



class MasterStudent(Student):
    """
    მაგისტრატურის სტუდენტთა კლასი, მემკვიდრეობით მიღებული სტუდენტური კლასიდან..
    """



def add_student(students):
#ახალ სტუდენტს ამატებს სტუდენტთა სიაში
    last_name = input("შეიყვანეთ სტუდენტის გვარი: ")
    first_name = input("შეიყვანეთ სტუდენტის სახელი: ")

    gender = input("შეიყვანეთ სტუდენტის სექსი (M - მამრობითი/F - მდედრობითი): ").upper()
    while gender not in ("M", "F"):
        print("არასწორია. შეიყვანეთ M ან F.")
        gender = input("შეიყვანეთ სქესი (M/F): ").upper()

    while True:
        try:
            roll_number = int(input("შეიყვანეთ სიის ნომერი: "))
            if roll_number not in [student.roll_number for student in students]:
                break
            else:
                print("ეს სიის ნომერი უკვე არსებობს. ეიყვანეთ უნიკალური ნომერი.")
        except ValueError:
            print("არასწორია. შეიყვანეთ რიცხვი")

    program = input("შეიყვანეთ სასწავლო პროგრამა: ")
    while True:
        try:
            year_of_study = int(input("შეიყვანეთ სასწავლო წელი (1-8): "))
            if 1 <= year_of_study <= 8:
                break
            else:
                print("სწავლის წელი არასწორია. გთხოვთ, შეიყვანოთ რიცხვი 1-დან 8-მდე.")
        except ValueError:
            print("სწავლის წელი არასწორია. გთხოვთ, შეიყვანოთ რიცხვი.")

    while True:
        year_of_enrollment = input("შეიყვანეთ სტუდენტის ჩარიცხვის წელი (ოთხნიშნა რიცხვი): ")
        if year_of_enrollment.isdigit() and len(year_of_enrollment) == 4:
            year_of_enrollment = int(year_of_enrollment)
            break
        else:
            print("ჩარიცხვის წელი არასწორია. გთხოვთ, შეიყვანოთ ოთხნიშნა რიცხვი.")

    while True:
        try:
            activity_max = int(input("განსაზღვრეთ აქტივობის მაქსიმალური ქულა: "))
            midterm_max = int(input("განსაზღვრეთ შუალედური გამოცდის მაქსიმალური ქულა: "))
            final_max = int(input("განსაზღვრეთ ფინალური გამოცდის მაქსიმალური ქულა: "))
            if (0 <= activity_max <= 100 and 0 <= midterm_max <= 100 and 0 <= final_max <= 100
                    and activity_max + midterm_max + final_max <= 100):
                break
            else:
                print("ქულების არასწორი განაწილება. აქტივობის, შუალედური და ფინალური გამოცდის ქულების ჯამი მაქსიმუმ 100 უნდა იყოს.")
        except ValueError:
            print("არასწორია. გთხოვთ, შეიყვანოთ მთელი რიცხვები.")

    while True:
        try:
            activity = int(input(f"რა ქულა მიიღო სტუდენტმა აქტივობაში? ({activity_max}-დან): "))
            midterm = int(input(f"რა ქულა მიიღო სტუდენტმა შუალედურ გამოცდაში? ({midterm_max}-დან): "))
            final = int(input(f"რა ქულა მიიღო სტუდენტმა ფინალურ გამოცდაში? ({final_max}-დან): "))
            if (0 <= activity <= activity_max and 0 <= midterm <= midterm_max and 0 <= final <= final_max):
                break
            else:
                print(f"არასწორია. ქულები არ უნდა აღემატებოდეს 100-ს.")
        except ValueError:
            print("არასწორია. გთხოვთ, შეიყვანოთ მთელი რიცხვები.")

    status = input("შეიყვანეთ სტუდენტის სტატუსი (აქტიური, შეჩერებული, გარიცხული): ").lower()
    while status not in ("აქტიური", "შეჩერებული", "გარიცხული" ):
        print("არასწორია. გთხოვთ, შეიყვანოთ „აქტიური“, „შეჩერებული“ ან „გარიცხული“.")
        status = input("შეიყვანეთ სტატუსი (აქტიური, შეჩერებული, გარიცხული): ").lower()

    degree_type = input("შეიყვანეთ პროგრამის ტიპი (B - ბაკალავრიატი, M - მაგისტრატურა): ").upper()
    if degree_type == 'B':
        student = BachelorStudent(last_name, first_name, gender, roll_number, program, year_of_study, year_of_enrollment, activity, midterm, final, status)
    elif degree_type == 'M':
        student = MasterStudent(last_name, first_name, gender, roll_number, program, year_of_study, year_of_enrollment, activity, midterm, final, status)
    else:
        print("არასწორია. შეიყვანეთ ან B ან M.")
        return

    students.append(student)
    print("სტუდენტის მონაცემები წარმატებით დაემატა!")
    save_to_csv(students)  # მონაცემებს ინახავს CSV ფაილში


def view_students(students):
    """
    აჩვენებს სიაში ყველა სტუდენტის მონაცემს.

    """
    if not students:
        print("სისტემაში ჯერ არ არის სტუდენტი.")
    else:
        students.sort(key=lambda student: student.roll_number)  # ახარიცხებს სიის ნომრების მიხედვით
        for student in students:
            print(student)
            print(f"საბოლოო ქულა: {student.calculate_total_grade()}")  # აჩვენებს საბოლოო ქულას
            print(f"GPA: {student.calculate_gpa()}")  # აჩვენებს GPA
    save_to_csv(students)


def search_student(students):
    """
    სტუდენტეის მოძებნა სიის ნომრის მიხედვით.

    """
    try:
        roll_number = int(input("მოსაძებნად შეიყვანეთ სტუდენტის ნომერი: "))
        for student in students:
            if student.roll_number == roll_number:
                print(student)
                print(f"საბოლოო ქულა: {student.calculate_total_grade()}")
                print(f"GPA: {student.calculate_gpa()}")
                return
        print("სტუდენტი არ მოიძებნა.")
    except ValueError:
        print("ნომერი არასწორია. გთხოვთ შეიყვანოთ მთელი რიცხვი.")
    save_to_csv(students)


def update_grade(students):
    """
    ააახლებს სტუდენტის მონაცემებს.

    """
    try:
        roll_number = int(input("მონაცემების განსაახლებლად შეიყვანეთ სტუდენტის ნომერი: "))
        for student in students:
            if student.roll_number == roll_number:
                while True:
                    try:
                        activity_max = int(input("განსაზღვრეთ აქტივობის მაქსიმალური ქულა: "))
                        midterm_max = int(input("განსაზღვრეთ შუალედური გამოცდის მაქსიმალური ქულა: "))
                        final_max = int(input("განსაზღვრეთ ფინალური გამოცდის მაქსიმალური ქულა: "))
                        if (0 <= activity_max <= 100 and 0 <= midterm_max <= 100 and 0 <= final_max <= 100
                                and activity_max + midterm_max + final_max <= 100):
                            break
                        else:
                            print("ქულების არასწორი განაწილება. აქტივობის, შუალედური და ფინალური გამოცდის ქულების ჯამი მაქსიმუმ 100 უნდა იყოს.")
                    except ValueError:
                        print("არასწორია. გთხოვთ, შეიყვანოთ მთელი რიცხვები.")

                while True:
                    try:
                        new_activity = int(input(f"რა ქულა მიიღო სტუდენტმა აქტივობაში? ({activity_max})-დან: "))
                        new_midterm = int(input(f"რა ქულა მიიღო სტუდენტმა შუალედურ გამოცდაში? ({midterm_max}-დან): "))
                        new_final = int(input(f"რა ქულა მიიღო სტუდენტმა ფინალურ გამოცდაში? ({final_max}-დან): "))
                        if (0 <= new_activity <= activity_max and 0 <= new_midterm <= midterm_max and 0 <= new_final <= final_max):
                            break
                        else:
                            print(f"არასწორია. ქულები არ უნდა აღემატებოდეს 100-ს.")
                    except ValueError:
                        print("არასწორია. გთხოვთ, შეიყვანოთ მთელი რიცხვები.")

                student.activity = new_activity
                student.midterm = new_midterm
                student.final = new_final
                print("მონაცემები წარმატებით განახლდა!")
                save_to_csv(students)
                return
        print("სტუდენტი არ მოიძებნა")
    except ValueError:
        print("ნომერი არასწორია. გთხოვთ შეიყვანოთ მთელი რიცხვი.")


def save_to_csv(students):
    """
    ინახავს სტუდენტის მონაცემებს CSV ფაილში.

    """
    with open('student_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Last Name", "First Name", "Gender", "Roll Number", "Program",
                         "Year of Study", "Year of Enrollment", "Activity", "Midterm", "Final", "Status", "Total Grade", "GPA"])
        for student in students:
            writer.writerow([student.last_name, student.first_name, student.gender, student.roll_number,
                             student.program, student.year_of_study, student.year_of_enrollment,
                             student.activity, student.midterm, student.final, student.status, student.calculate_total_grade(), student.calculate_gpa()])


def main():
    """
    სტუდენტის მართვის სისტემის გაშვების მთავარი ფუნქცია.
    """
    students = []

    while True:
        print("\nსტუდენტების მართვის სისტემა")
        print("1. დაამატეთ ახალი სტუდენტი")
        print("2. ყველა სტუდენტის ნახვა")
        print("3. მოძებნეთ სტუდენტი ნომრის მიხედვით")
        print("4. განაახლეთ სტუდენტის შეფასება")
        print("5. გამოსვლა")

        choice = input("შეიყვანეთ ციფრი 1-დან 5-ის ჩათვლით: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            update_grade(students)
        elif choice == '5':
            print("გამოსვლა...")
            break
        else:
            print("არასწორია. აირჩიეთ ჩამოთვლილიდან.")

if __name__ == "__main__":
    main()