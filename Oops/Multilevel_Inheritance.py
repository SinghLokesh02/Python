# Multilevel Inheritance

'''
Multilevel inheritance, the features that are part of the original class, as well as the class that is derived from it, are passed on to the new class. It is similar to a relationship involving grandparents and children.

'''

# Example - 1

print("\n\nThis is Example 1 of Multilevel Inheritance of Python\n\n")
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



# Example - 2
print("\n\nThis is Example 2 of Multilevel Inheritance of Python\n\n")

# Python program for demonstrating multilevel inheritance  
  
# Here, we will create the Base class   
class Grandfather1:  
  
    def __init__(self, grandfathername1):  
        self.grandfathername1 = grandfathername1  
  
# here, we will create the Intermediate class  
class Father1(Grandfather1):  
    def __init__(self, fathername1, grandfathername1):  
        self.fathername1 = fathername1  
  
        # here, we will invoke the constructor of Grandfather class  
        Grandfather1.__init__(self, grandfathername1)  
  
# here, we will create the Derived class  
class Son1(Father1):  
    def __init__(self,sonname1, fathername1, grandfathername1):  
        self.sonname1 = sonname1  
  
        # here, we will invoke the constructor of Father class  
        Father1.__init__(self, fathername1, grandfathername1)  
  
    def print_name(self):  
        print('Grandfather name is :', self.grandfathername1)  
        print("Father name is :", self.fathername1)  
        print("Son name is :", self.sonname1)  
  
# Driver code  
s1 = Son1('John', 'John Jr', 'John Jr Jr')  
print (s1.grandfathername1)  
s1.print_name()  