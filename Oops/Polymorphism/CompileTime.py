# Compile Time Polymorphism

# Method Overloading -> Compile Time Polymorphism
# Method Overloading is not supported in Python
# But we can achieve it with the help of default arguments and with the help of the variable length arguments


class Class:
    def Sum(self, a=None, b=None ,c = None, d = None):
        s = 0
        if a!=None and b!=None and c!=None and d!=None:
            s = a+b+c+d
        elif a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        print(s)


a = Class()
a.Sum(7, 8)

a.Sum(3, 4, 5)

a.Sum(3, 4, 5, 6)
