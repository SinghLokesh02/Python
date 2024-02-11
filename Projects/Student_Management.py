import time
class Student:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.roll_no = ""
        self.number = ""
        
    def Create_new_student(self):
        self.name = input("Enter student name: ")
        self.age = input("Enter student age: ")
        self.roll_no = input("Enter student roll no: ")
        self.number = input("Enter student number: ")
        
    def Display_student(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Roll no: ", self.roll_no)
        print("Number: ", self.number)
    
    def Update_student(self):
        update = input("Enter the field you want to update: ")
        
        if update == "name":
            self.name = input("Enter new name: ")
        elif update == "age":
            self.age = input("Enter new age: ")
        elif update == "roll_no":
            self.roll_no = input("Enter new roll no: ")
        elif update == "number":
            self.number = input("Enter new number: ")
    
    def Delete_student(self):
        delete = input("Enter the field you want to delete: ")
        
        if delete == "name":
            self.name = ""
        elif delete == "age":
            self.age = ""
        elif delete == "roll_no":
            self.roll_no = ""
        elif delete == "number":
            self.number = ""
        
        
print("\n===== Student Management System =====")
time.sleep(2)

list_of_students = {}
n = 0 
while (n != 5):
    print("\n\n1. Create new student")
    print("2. Display student")
    print("3. Update student details")
    print("4. Delete student Details")
    print("5. Exit")
    n = int(input("Enter your choice: "))
    # If User wants to exit at the start
    if n == 5:
        break
    
    name = input("Enter student name for which you want to perform Operation: ")
    
    if name not in list_of_students:
        list_of_students[name] = Student()  
    
    if n == 1:
        list_of_students[name].Create_new_student()
    
    elif n == 2:
        list_of_students[name].Display_student()
        
    elif n == 3:
        list_of_students[name].Update_student()
        
    elif n == 4:
        list_of_students[name].Delete_student()
    

        
    
    