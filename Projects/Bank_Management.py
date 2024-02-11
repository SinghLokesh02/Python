# Bank Management System

import os
import sys
import time
import random
import datetime


# Main Menu
  
class Atm:
    def __init__(self) -> None:
        self.__balance = 0
        self.__pin = ""
        # self.Menu()
    
   

    def CreatePin(self):
        pin = input("Enter Your Password : ")
        self.__pin = pin


    # Method For Money Deposit
    def Deposit(self):
        pin = input("Enter Your Password : ")
        if pin == self.__pin:
            amount = int(input("Enter the amount for deposit : "))
            self.__balance += amount
            print("Amount Deposited Successfully ✅✅")
        else:
            print("Invalid Password ❌❌")


    # Method For Money Withdrawal
    def Withdrawal(self):
        pin = input("Enter Your Password : ")
        if pin == self.__pin:
            amount = int(input("Enter the amount  : "))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal Successful ✅")
            else:
                print("Insufficient __Balance 🤑💷")
        else:
            print("Invalid Password ❌❌")

    # Method For Check Bank __Balance
    def Check___Balance(self):
        pin = input("Enter Your Password : ")
        if pin == self.__pin:
            print("The Available __Balance is : ", self.__balance)
        else:
            print("Invalid Password ❌❌")

    # Method For Program Over
    def Done(self):
        print("The Program is Over Now 😊✅✅")



# Main Function
if __name__ == "__main__":
    My_bank_collection = {}
    print(
        """
        =================================
        Welcome to Bank Management System
        =================================
        """
        )
    time.sleep(1)
    while True:
        print("""
                Hello, How would You like to Proceed
                1 : Create Pin
                2 : Deposit
                3 : Withdrawal
                4 : Check __Balance
                5 : Exit
                """)
                
        userinput = int(input("Enter Your Choice : "))
        name = input("Enter Your Name : ")
        if name not in My_bank_collection:
            My_bank_collection[name] = Atm()
        else:
            print("Welcome Back", name)
        if userinput == 5:
            My_bank_collection[name].Done()
            break
        elif userinput == 1:
            My_bank_collection[name].CreatePin()
        elif userinput == 2:
            My_bank_collection[name].Deposit()
        elif userinput == 3:
            My_bank_collection[name].Withdrawal()
        elif userinput == 4:
            My_bank_collection[name].Check___Balance()
        
    
    
    