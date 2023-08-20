# Python hasattr() Function
'''
Syntax
hasattr(object, attribute)

Parameter Values
    Parameter	                      Description
    object	                          Required. An object.
    attribute	                      The name of the attribute you want to check if exists

'''

class Person:
    name = "Lokesh Singh"
    age = 21
    address = "Makhdoompur, Ambedkarnagar, UP"
    contact = 7985218363
    

lokesh = Person()
x = hasattr(lokesh,'friend')
# Because friend is not defined in Person class so it will return False
print(x) # -> False




setattr(lokesh,'friend',"Sonali Singh")
x = hasattr(lokesh,'friend')
# Because friend is defined in Person by setattr method in the class so it will return True
print(x) # -> True





################################ Python delattr() Function ################################
'''
Definition and Usage
The delattr() function will delete the specified attribute from the specified object.

Parameter Values
    Parameter	            Description
    object	                Required. An object.
    attribute	            Required. The name of the attribute you want to remove
'''

class Employee:
    name = "Lokesh Singh"
    age = 21
    address = "Makhdoompur, Ambedkarnagar, UP"
    contact = 7985218363
    salary = 15000
    
    
lokesh = Employee()
print("Before deleting the attribute")
print(hasattr(lokesh,'salary')) # -> True

delattr(Employee,'salary')
print("After deleting the attribute")
print(hasattr(lokesh,'salary')) # -> False
    