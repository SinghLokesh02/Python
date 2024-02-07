# Example of Multiple Inheritance

# Base Class
class Base:
    # Constructor to set Data
    def __init__(self, name, roll, role):
        self.name = name
        self.roll = roll
        self.role = role


# Intermediate Class: Inherits the Base Class
class Intermediate(Base):
    # Constructor to set age
    def __init__(self, age, name, roll, role):
        super().__init__(name, roll, role)
        self.age = age


# Derived Class: Inherits the Intermediate Class
class Derived(Intermediate):
    # Method to Print Data
    def __init__(self, age, name, roll, role):
        super().__init__(age, name, roll, role)

    def Print_Data(self):
        print(f"The Name is : {self.name}")
        print(f"The Age is : {self.age}")
        print(f"The role is : {self.role}")
        print(f"The Roll is : {self.roll}")


# Creating Object of Base Class
obj = Derived(21, "Lokesh Singh", 25, "Software Trainer")

# Printing the data with the help of derived class
obj.Print_Data()