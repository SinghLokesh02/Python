# Adding Additional Methods

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} can produce sound")


class Bird(Animal):
    def Fly(self):
        print(f"{self.name} can fly as well")


bird = Bird("Sparrow")
bird.sound()
bird.Fly()



# Method - 3: Using Contructor and Additional Attributes

class Animal:
    def __init__(self,name):
        self.name = name

    def Sound(self):
        print(f"{self.name} can produce sound")


class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed

    def Play(self):
        print(f"{self.name} can play with us")


dog = Dog("Jimmy","Pitbull")
dog.Sound()
dog.Play()


# Method - 3: Overriding Methods
class Animal:
    def __init__(self, name):
        self.name = name

    def Sound(self):
        print(f"{self.name} can produce sound")


class Dog(Animal):
    def Sound(self):
        print(f"{self.name} barks")


obj = Dog("Jimmy")
obj.Sound()
