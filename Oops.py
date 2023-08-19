# Example - 1
class add:
    def sum(self):
        return self.a + self.b


num = add()
num.a = 10
num.b = 20
# print(num.sum())
s = num.sum()
print("The sum of 2 number is : ", s)


# Exammple - 2
class student:
    def data(self):
        print("The name of the student is : ", self.name)
        print("The roll no of the student is : ", self.roll)
        print("The marks of the student is : ", self.marks)


nazim = student()
nazim.name = "nazim"
nazim.marks = 100
nazim.roll = 78
nazim.data()


# Constructor in python


class Student:
    name = "Lokesh Singh"
    roll = 25
    address = "RJ"
    Company = "Technoglobe"

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        

    def print(self):
        print("The name is ", self.name)
        print("The roll is ", self.roll)
        print("The Address is ", self.address)
        print("The Company is ", self.Company)


lokesh = Student("lokesh",25)
lokesh.print()


sonali = Student("sonali",59)
sonali.Company = "AICTE"
sonali.address = "Delhi"
sonali.print()



# About self in python
class Employee:
    Company = "Technoglobe"
    def printSalaray(self):
        print("The salary is 20k")

lokesh = Employee()
lokesh.printSalaray()
# TypeError: Employee.printSalaray() takes 0 positional arguments but 1 was given
# lokesh.printsalary = Employee.salary(lokesh) that why we have to pass self in the class methdos,that's why it was saying that 1 positional argument given



