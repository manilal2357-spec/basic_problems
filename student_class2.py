class Student:
    all_students = []

    def __init__(self, name, roll_number, set, CGPA):
        self.name = name
        self.roll_number = roll_number
        self.set = set
        self.cgpa = CGPA

        Student.all_students.append(self)

    def __str__(self):
        return (f"Name: {self.name}, "
                f"Roll No: {self.roll_number}, "
                f"Set: {self.set}, "
                f"CGPA: {self.cgpa}")


student_1 = Student("manilal", 24, "A", 7.4)
student_2 = Student("ram", 25, "B", 7.9)
student_3 = Student("shyam", 26, "C", 8.1)

for student in Student.all_students:
    print(student)