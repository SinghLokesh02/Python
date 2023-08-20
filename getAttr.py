# Python getattr() Function


# Definition and Usage
# The getattr() function returns the value of the specified attribute from the specified object.

class Person:
    name = "Lokesh Singh"
    age = 21
    address = "Makhdoompur, Ambedkarnagar, UP"
    contact = 7985218363
    

x = getattr(Person,'age')
y = getattr(Person,'contact')
print(x)
print(y)

# z = getattr(Person,'friend') This will show error

# AttributeError: type object 'Person' has no attribute 'girlfriend'. This message is printed if there is no attribute defined as you are searching for so if You want to see no error then you can pass default message as well if attribute is not there is a class then the default message will be printed

z = getattr(Person,'friend',"Sonali Kumari") # -> This will not becaues here deafault message is given
print(z)

'''
Syntax
getattr(object, attribute, default)

Parameter Values

Parameter	                   Description
object	                       Required. An object.
attribute	                   The name of the attribute you want to get the value from
default	                       Optional. The value to return if the attribute does not exist

'''