print("This file contains code of Multiple Inheritance in Python")

'''

Multiple Inheritance If a class is able to be created from multiple base classes, this kind of Inheritance is known as multiple Inheritance. When there is multiple Inheritance, each of the attributes that are present in the classes of the base has been passed on to the class that is derived from it.

'''


# Multiple Inheritance
print("\n\nThis is Example 1 of Multiple Inheritance of Python\n\n")

class A1:
    a = 10
    
class B1:
    b = 23

class C1(B1,A1):
    def show(self):
        print(f"The value of a is {self.a}")
        print(f"The value of b is {self.b}")
        print(f"The value of a+b is {self.b+self.a}")
        

# Creating Objects
num = C1()
num.show()
print()



# Example - 2
print("\n\nThis is Example 1 of Multiple Inheritance of Python\n\n")

class Father:
    namef = "Mr Ved Prakash Singh"
    agef = 50
    occupationf = "BSF SI"
    salaryf = 50000
    def __init__(self):
        print("\nThis is Father Class\n")
        print(f"Name of Father is {self.namef}")
        print(f"Age of Father is {self.agef}")
        print(f"Occupation of Father is {self.occupationf}")
        print(f"Salary of Father is {self.salaryf}")
    
    
class Mother:
    name_m = "Mrs Vidya Singh"
    age_m = 48
    occupation_m = "Housewife"
    salary_m = 0
    def Print(self):
        print("\nThis is Mother Class\n")
        print(f"Name of Mother is {self.name_m}")
        print(f"Age of Mother is {self.age_m}")
        print(f"Occupation of Mother is {self.occupation_m}")
        print(f"Salary of Mother is {self.salary_m}")
    
    
class child(Father,Mother):
    name = "Lokesh Singh"
    age = 24
    occupation = "Student"
    salary = 0
    def __init__(self):
        print("\nThis is Child Class\n")
        print(f"Name of Child is {self.name}")
        print(f"Age of Child is {self.age}")
        print(f"Occupation of Child is {self.occupation}")
        print(f"Salary of Child is {self.salary}")
        super().__init__()
        

# Creating Objects
lokesh = child()
lokesh.Print()
print()