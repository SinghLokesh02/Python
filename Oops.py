# Example - 1
class add:
    def sum(self):
        return self.a+self.b
    
num = add()
num.a = 10
num.b = 20
# print(num.sum())
s = num.sum()
print("The sum of 2 number is : ",s)


# Exammple - 2
class student:
    def data(self):
        print("The name of the student is : ",self.name)
        print("The roll no of the student is : ",self.roll)
        print("The marks of the student is : ",self.marks)
        

nazim = student()
nazim.name = "nazim"
nazim.marks = 100
nazim.roll = 78

nazim.data()