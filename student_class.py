class Student:
    def __init__(self,name,roll_number,set,CGPA):
        self.name = name
        self.roll_number = roll_number
        self.set = set
        self.cgpa = CGPA
        self.print_details()
        print("")
    def print_details(self):
        print("hi!",self.name)
        print("your roll number is :-",self.roll_number)
        print(f"you are in {self.set} set ")
        print(f"your cgpa is :- {self.cgpa}")
student_1 = Student("manilal",24,"A",7.4)
student_2 = Student("ram",25,"B",7.9)
student_3 = Student("shyam",20,"B",7)
 


