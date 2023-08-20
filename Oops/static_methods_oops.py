# Static method
'''
What is the Static Method in Python?
A static method does not receive an implicit first argument. A static method is also a method that is bound to the class and not the object of the class. This method can’t access or modify the class state. It is present in a class because it makes sense for the method to be present in class.

Syntax Python Static Method: 
class C(object):
    @staticmethod
    def fun(arg1, arg2, ...):
        ...
returns: a static method for function fun.


Class method vs Static Method
The difference between the Class method and the static method is:

A class method takes cls as the first parameter while a static method needs no specific parameters.
A class method can access or modify the class state while a static method can’t access or modify it.
In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.
'''
class student:
    salary = 20000
    add = "RJ"
    name = "xyz"
    def set(self,name,add):
        self.name = name
        self.add = add
    
    def print(self):
        print("The name of student is : ",self.name)
        print("The Address of student is : ",self.add)
        print("The salary of student is : ",self.salary)
        
    @staticmethod
    def greet():
        print("Hello Good Morning")
    
lokesh = student()
lokesh.set("Lokesh","UP")
lokesh.print()

lokesh.greet()