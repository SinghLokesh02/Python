# Super Class
class Base:
    def __init__(self, name, roll, age):
        self.name = name
        self.roll = roll
        self.age = age


# Sub Class
class Sub(Base):

    def __init__(self, name, roll, age):
        super().__init__(name, roll, age)

    # Now Sub class has all the attributes of Base class
    def display(self):
        print(f" Name: {self.name}\n Roll: {self.roll}\n Age: {self.age}")


# Creating object of Sub class
obj = Sub("Sonali", 58, 24)
obj.display()
