class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} has enrolled in {course}.")

    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("ჩარიცხული კურსები:")
        if self.courses:
            for course in self.courses:
                print(f"- {course}")
        else:
            print("ჯერ არც ერთ კურსში არაა სტუდენტი ჩარიცხული.")


student1 = Student("გიორგი გიორგაძე", "12345")
student2 = Student("ნინო კაპანაძე", "67890")

student1.enroll("პროგრამირების საფუძვლები")
student1.enroll("ექსელის კურსი")
student2.enroll("გრაფიკული დიზაინი")
student2.enroll("ინგლისური ენა")

student1.display_student_info()
print()
student2.display_student_info()