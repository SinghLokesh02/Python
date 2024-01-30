# Dynamic Calculator

def Sum():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum of two numbers is: ", a+b)

def Sub():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Subtraction of two numbers is: ", a-b)

def Mul():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Multiplication of two numbers is: ", a*b)

def Div():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Division of two numbers is: ", a/b)
    
choice = 0
while(choice != 5):
    print("\n\n1: Add")
    print("2: Substract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")

    choice  = int(input("Enter Your Choice : "))
    if(choice == 1):
        Sum()
    elif(choice == 2):
        Sub()
    elif(choice == 3):
        Mul()
    elif(choice == 4):
        Div()
    elif(choice >= 5):
        break

print("The Program is Over 😊😊👍")
    

