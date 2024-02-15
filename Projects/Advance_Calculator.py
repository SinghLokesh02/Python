# Advance Calculator using Python

import math, time


print("\n\n============= Advance Calcultor =============\n\n")
time.sleep(2)


def Sum(a, b):
    sum = a + b
    print(f"\nThe Addition of {a} and {b} is :", sum)


def Sub(a, b):
    sub = a - b
    print(f"\nThe Subtraction of {a} and {b} is :", sub)


def Mul(a, b):
    mul = a * b
    print(f"\nThe Multiplication of {a} and {b} is :", mul)


def Div(a, b):
    div = a / b
    print(f"\nThe Division of {a} and {b} is :", div)


def Mod(a, b):
    mod = a % b
    print(f"\nThe Modulus of {a} and {b} is :", mod)


def even_odd():
    a = input("\nEnter any Number : ")
    if a.isdigit() == True:
        a = int(a)
        if a % 2 == 0:
            print(f"\nThe {a} Is Even")
        else:
            print(f"\nThe {a} IS Odd")
    else:
        print("\n\nPlease Enter Valid Data ❌❌")


def LCM(a, b):
    # LCM = a*b/hcf
    hcf = math.gcd(a, b)
    lcm = (a * b) / hcf
    print(f"The LCM of {a} and {b} is : {lcm}")


def HCF(a, b):
    hcf = math.gcd(a, b)
    print(f"The HCF of {a} and {b} is : {hcf}")


def Squareroot():
    a = input("\nEnter any Number : ")
    if a.isdigit() == True:
        a = int(a)
        ans = math.sqrt(a)
        print(f"The Square Root of {a} is : {ans}")
    else:
        print("\n\nPlease Enter Valid Data ❌❌")


def Percentage(a, b):
    ans = (a / b) * 100
    print(f"The Percentage is : {ans}%")


choice = 0
print("<===-  WELCOME TO MY PROJECT -===>")
while choice != 11:
    print("\n\n1: Addition: ")
    print("2: Subtraction: ")
    print("3: Multipication: ")
    print("4: Division: ")
    print("5: Modulus: ")
    print("6: Check Even Or Odd: ")
    print("7: LCM")
    print("8: HCF")
    print("9: Square Root")
    print("10: Percentage")
    print("11: Break:\n")

    choice = int(input("Enter your Choice: "))

    if choice >= 11:
        break

    # If the case is 6 or 9
    if choice == 6:
        even_odd()
    elif choice == 9:
        Squareroot()

    # If Choice Not Equals to 6 and 9 Because We have Already Handled it.
    if choice != 6 and choice != 9:
        try:
            a = input("\nEnter First Number: ")
            b = input("Enter Second Number: ")
            a = int(a)
            b = int(b)
        except:
            print("Wrong Input ❌❌")
        else:
            if choice == 1:
                Sum(a, b)
            elif choice == 2:
                Sub(a, b)
            elif choice == 3:
                Mul(a, b)
            elif choice == 4:
                Div(a, b)
            elif choice == 5:
                Mod(a, b)
            elif choice == 7:
                LCM(a, b)
            elif choice == 8:
                HCF(a, b)
            elif choice == 10:
                Percentage(a, b)


print("THE PROGRAM IS OVER NOW ✔️✅👍 !!")
