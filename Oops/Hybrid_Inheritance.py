# Hybrid Inheritance

'''
It combines multiple inheritances with multilevel inheritance. A class can have two or more parent classes, but only one of them can have derived classes.

'''

# Python program to demonstrate hybrid inheritance

class Office:

    def func1(self):
        print ('This function is in Office.')

class Emp1(Office):

    def func2(self):
        print ('This function is in Employee 1.')

class Emp2:

    def func3(self):
        print ('This function is in Employee 2.')

class Emp3(Emp1, Emp2):

    def func4(self):
        print ('This function is in Employee 3.')

# Driver's code

object = Emp3()
object.func1()
object.func2()