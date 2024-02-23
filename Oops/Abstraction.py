# Abstraction in Python

# Abstract class in Python is a class that contains one or more abstract methods. An abstract method is a method that is declared, but contains no implementation. Abstract classes may not be instantiated, and its abstract methods must be implemented by its subclasses.

# An abstract class is a class that generally provides incomplete functionality and contains one or more abstract methods. Abstract methods are the methods that generally don’t have any implementation, it is left to the sub classes to provide implementation for the abstract methods.

# Python provides a module called abc (Abstract Base Class) which provides the base for defining Abstract Base classes. The abc module in Python provides the infrastructure for defining custom abstract base classes (ABCs).

# The abc module in Python provides the metaclass ABCMeta which is used to create an abstract class. The ABCMeta is a class that when called, returns a new class object. The abstract class is created by deriving the metaclass from ABCMeta and then the abstract class is derived from the base class.

# Abstract methods are the methods that generally don’t have any implementation, it is left to the sub classes to provide implementation for the abstract methods.

# The abstract method can be defined by using the @abstractmethod decorator. The abstract method can be defined by using the @abstractmethod decorator.


# Abstract class can have both normal(concrete) methods and abstract methods. The abstract class can have a normal method with an abstract method. The abstract class can have a concrete method with an abstract method.


# Abstract class must have atleast one abstract method.

# An abstract class also called blue print for other classes. It allows you to define a signature for a method, but not the implementation.

# All abstract methods should be implemented in the child class. Else it will throw an error. and the child class will also become an abstract class.


from abc import ABC, abstractmethod


class Parent(ABC):
    def Property(self):
        print("I have Property of 10000000")

    @abstractmethod
    def FirstEarnMoney(self):
        pass


class Child1(Parent):

    def Introduction(self, name):
        print(f"My name is : {self.name}")


class Child2(Parent):

    def __init__(self, name):
        self.name = name

    def Introduction(self):
        print(f"My name is : {self.name}")

    def FirstEarnMoney(self):
        print("I Have Earned Money of 100000")


Amit = Child2("Amit")
Amit.Introduction()
Amit.Property()
