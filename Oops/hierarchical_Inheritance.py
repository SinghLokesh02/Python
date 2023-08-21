print("This file contains the code of hierarchical Inheritance in Python")

'''
Hierarchical Inheritance If multiple derived classes are created from the same base, this kind of Inheritance is known as hierarchical inheritance. In this instance, we have two base classes as a parent (base) class as well as two children (derived) classes.
'''


# Example - 1
print("\nThis is Example 1 of Hierarchical Inheritance\n")
class Main:
    father_name = "Father Name"
    mother_name = "Mother Name"
    Address = "UP"
    house_num = 112


class Child1(Main):
    name = "child1"
    def __init__(self):
        print("\nPrinting the details of Child1 Class\n")
        print("The name is : ",self.name)
        print("The father name is : ",self.father_name)
        print("The mother name is : ",self.mother_name)
        print("The Address name is : ",self.Address)
        print("The House number is : ",self.house_num)
        
        
class Child2(Main):
    name = "child2"
    def __init__(self):
        print("\nPrinting the details of Child2 Class\n")
        print("The name is : ",self.name)
        print("The father name is : ",self.father_name)
        print("The mother name is : ",self.mother_name)
        print("The Address name is : ",self.Address)
        print("The House number is : ",self.house_num)


# Creating the object for the class

amit = Child1()
lokesh = Child2()



# Example - 2 of hierarchical Inheritance
print("\nThis is Example 2 of Hierarchical Inheritance\n")
class Number:
    num1 = 10
    num2 = 20
    def operations():
        pass
        
class Addition(Number):
    def operations(self):
        print("The addition is : ",self.num1 + self.num2)
        
class Subtraction(Number):
    def operations(self):
        print("The Subtraction is : ",self.num1 - self.num2)
        
class product(Number):
    def operations(self):
        print("The Multiplication is : ",self.num1 * self.num2)


# Creating the object for the class
a = Addition()
a.operations()


s = Subtraction()
s.operations()


m = product()
m.operations()
print()