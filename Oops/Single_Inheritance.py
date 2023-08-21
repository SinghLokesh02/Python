# Inheritance

'''
Inheritance is the capacity of a particular class to obtain or inherit properties from another class and then use them when required. Inheritance has the following characteristics:

It is an excellent representation of relationships in the real world.
It allows code reuse. It doesn't require us to create the same code repeatedly and again. It also allows us to add options to an existing class without having to modify the existing code.
It is a transitive nature, meaning that if B is inherited from another class A, all the subclasses belonging to B will inherit directly from class A.

'''
# Basic Single Inheritance
'''
The types of inheritance depend on the number of children and parents involved. There are four kinds of inheritance available in Python:

Single Inheritance Single inheritance allows a derivate class to inherit properties of one parent class, and this allows code reuse and the introduction of additional features in existing code.
'''
print("\n\nThis is Example of Single Inheritance of Python\n\n")
class Number:
    a = 10
    b = 20
    def print(self):
        print(f"The value of a is :{self.a}")
        print(f"The value of a is :{self.b}")
        
        
class Add(Number):
    def sum(self):
        super().print() # This is used to call the print function of the parent class
        print(f"The sum of values is :{self.a+self.b}")


n = Add()
n.sum()





