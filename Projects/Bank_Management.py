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
        self.Menu()
    
    def Menu(self):
        print(
        """
        ==============================
        Welcome to Bank Management System
        ==============================
        """
        )
        time.sleep(1)
        print("""
              Hello, How would You like to Proceed
               1 : Create Pin
               2 : Deposit
               3 : Withdrawal
               4 : Check __Balance
               5 : Exit
              """)
             
        userinput = int(input("Enter Your Choice : "))
        if userinput == 1:
            self.CreatePin()
        elif userinput == 2:
            self.Deposit()
        elif userinput == 3:
            self.Withdrawal()
        elif userinput == 4:
            self.Check___Balance()
        elif userinput == 5:
            self.Done()

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



sbi = Atm()