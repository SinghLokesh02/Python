# Can be Achieved with the help of Method Overriding

# Rules for Runtime
# 1) Method should not be in same name
# 2) Method declaration should be same, but the definition will be change


class Student:
    def __init__(self, name, role, roll):
        self.name = name
        self.roll = roll
        self.role = role

    def Print_details(self):
        print(f"The Name of Student is {self.name}")
        print(f"The Roll Number of Student is {self.roll}")
        print(f"The Role of Student is {self.role}")


class Teacher(Student):
    Name = "Yograj Sharma"
    Role = "HOD"
    Subject = "DSA"

    def __init__(self, name, role, roll):
        super().__init__(name, role, roll)

    def Print_details(self):
        print(f"The Name of Teacher is : {self.Name}")
        print(f"The Role of Teacher is : {self.Role}")
        print(f"The Subject of Teacher is : {self.Subject}")


yogi = Teacher("Lokesh Singh", "Trainer", 25)
yogi.Print_details()

base = Student("Lokesh Singh", "Trainer", 25)
base.Print_details()
