# Inheritance


# Basic Single Inheritance
print("\n\nThis is Example of Single Inheritance of Python\n\n")
class Number:
    a = 10
    b = 20
    def print(self):
        print(f"The value of a is :{self.a}")
        print(f"The value of a is :{self.b}")
        
        
class Add(Number):
    def sum(self):
        print(f"The sum of values is :{self.a+self.b}")


n = Add()
n.sum()



# Multilevel Inheritance
print("\n\nThis is Example of Multilevel Inheritance of Python\n\n")
class A:
    a = 70
    
class B(A):
    b = 50

class C(B):
    def show(self):
        print(f"The value of a is {self.a}")
        print(f"The value of b is {self.b}")
        print(f"The value of a+b is {self.a+self.b}")
        

# Creating Objects 
num = C()
num.show()


# Multiple Inheritance
print("\n\nThis is Example of Multiple Inheritance of Python\n\n")

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