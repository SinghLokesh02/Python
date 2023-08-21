'''
Definition and Usage
The super() function is used to give access to methods and properties of a parent or sibling class.

The super() function returns an object that represents the parent class.

'''

class ParentClass:
    def parentMethod(self):
        print("This is Parent class Method")
        

class ChildClass(ParentClass):
    def parentMethod(self):
        print("This is child class parent Method")
        super().parentMethod()
        
    def childMethod(self):
        print("This is Child class Method")
        super().parentMethod()
    
    
childobj = ChildClass()
childobj.childMethod()
childobj.parentMethod()