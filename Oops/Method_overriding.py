'''
Prerequisite: Inheritance in Python

Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes. When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) as a method in its super-class, then the method in the subclass is said to override the method in the super-class.

'''

                                            # Example - 1

class Father:
    name = "father"
    age = 50
    color = "fair"
    def Color(self):
        print("The color of the father is : ",self.color)
    
class Child(Father):
    name = "child"
    age = 18
    color = "white"
    def Color(self):
        print("The color of the child is : ",self.color)
        
        
# Object Creation
rakesh = Father()
rakesh.Color()

# child class object
suresh = Child()
suresh.Color()
        
        
        


                                            # Example - 2

class Num1:
    num1 = 32
    num2 = 2
    def Operation(self):
        print("The sum of two number is : ",self.num1+self.num2)
        


class Num2(Num1):
    def Operation(self):
        print("The Multiplication of two number is : ",self.num1*self.num2)


new_obj1 = Num1()
new_obj1.Operation()


new_obj2 = Num2()
new_obj2.Operation()


