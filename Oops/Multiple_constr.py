'''
In Python, you cannot define multiple constructors with different signatures in the same class. When you define multiple __init__ methods in a class, the last one defined will override the previous ones. This is why you're getting an error when trying to create an instance of the class with no arguments, even though you have a default constructor.

class lokesh:
    def __init__(self):
        print("Default")
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("constructor 2")
        
l = lokesh() # This will show error

To achieve what you want, you can provide default values for the parameters in the constructor:
        
'''

class Lokesh:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
        print("Constructor")

# Creating an instance without arguments
l1 = Lokesh()

# Creating an instance with arguments
l2 = Lokesh("John", 25)
print(l2.name)
print(l2.age)
        

