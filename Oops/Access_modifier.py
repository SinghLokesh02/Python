'''
Access Specifiers/Modifiers
Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.

Let us see the each one of access specifiers in detail:

Types of access specifiers

Public access modifier
Private access modifier
Protected access modifier

'''

class Student:
    def __init__(self):
        self.name = "Lokesh Singh" # public can be accessed outside
        self.__roll = 23
        
lokesh = Student()

print(lokesh.name)
# print(lokesh.__roll)#Cannot be accessed from outside directly as the tag of private is given
print(lokesh._Student__roll)#Can be accessed from outside Indirectly as the tag of private is given

'''
normal name -> Public Access Modifier
_normal name -> Protected Access Modifier
__normal name -> private Access Modifier
'''