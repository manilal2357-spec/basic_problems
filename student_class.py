class Student:
    def __init__(self,name,roll_number,set,CGPA):
        self.name = name
        self.roll_number = roll_number
        self.set = set
        self.cgpa = CGPA
    def print_details(name):
        print("hi!",name.name)
        print("your roll number is :-",name.roll_number)
        print(f"you are in {name.set} set ")
        print(f"your cgpa is :- {name.cgpa}")
student_1 = Student("manilal",24,"A",7.4)
student_1.print_details()
