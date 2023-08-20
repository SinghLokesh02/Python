# Set Attribute in Python

# Definition and Usage
# The setattr() function sets the value of the specified attribute of the specified object.

'''
Syntax
setattr(object, attribute, value)

    Parameter Values
        Parameter	            Description
        object	                Required. An object.
        attribute	            Required. The name of the attribute you want to set
        value	                Required. The value you want to give the specified attribute

'''

class Person:
    name = "Lokesh Singh"
    age = 21
    address = "Makhdoompur, Ambedkarnagar, UP"
    contact = 7985218363
    
    def print_data(self):
        print("Person Details: ")
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Address: ",self.address)
        print("Contact: ",self.contact)
        print("Friend: ",self.friend)
        print()
        
        
        
    

lokesh = Person()
setattr(lokesh,'friend',"Sonali Singh")
setattr(lokesh,'Best_friend',"Diwakar Singh Chauhan")
print(getattr(lokesh,'Best_friend'))
lokesh.print_data()


sonali = Person()
sonali.name = "Sonali Singh"
sonali.age = 23
sonali.address = "Patna,Bihar"
setattr(sonali,'friend',"Lokesh Singh")
setattr(sonali,'contact',"9318485949")
sonali.print_data()


# Set Attribute in Python
# The setattr() function sets the value of the specified attribute of the specified object.
