# Creating a Class


class Student:
    name = "Lokesh Singh"  # Public Attribute
    __id = 1234  # Private Attributes

    # Method for Printing Private Attribute
    def Print_Id(self):
        print(f"The Id of student is : {self.__id}")


# Creating Object of Class

lokesh = Student()

print(lokesh.name)  # Public Attribute can be accessed directly from outside class

# Private Attribute cannot be accessed directly from outside class
# print(lokesh.__id) This will raise an AttributeError

# Accessing private attribute using getter method
lokesh.Print_Id()

# Accessing private attribute using class name
print("Printing the Private Member of the class : ", lokesh._Student__id)  # This is called name mangling
