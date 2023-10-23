# ********************************* List **************************************************

list = [1,2,3,4,543,543,21,65,678]

for i in list:
    print(i)
    
for i in range(0,len(list),2):
    print(list[i])

# ********************************* Tuples *************************************************

st = (1,2,3,4,5,6,3,3)
# Print the tuple
print(st)

# Print the length of the tuple
print(len(st))

# Print the Element of the tuple by Index
print(st[1])

# You cannot change the element of the tuple once declared
st[1] = 89
print(st)

# Methods of the tuple

# Return the Number of element present in the set
print(st.count(3))

# Find the element by the index in tuple
print(st.index(3))

# If You want to perform any other operation on tuple then you have to first convert it into list
 
# ********************************* Set ***************************************************
# In this we cannot store duplicate data
set = {1,2,3,4,5,7,7}
print(set)

# Add item to the set
set.add(89)
print(set)

# Remove Item from the set
set.remove(7)
print(set)

# Print the length of the set
print(len(set))

# Print the type
print(type(set))

# Print set item Using Loop
for x in set:
    print(x)
    
# Pop method in set -> 	Removes an element from the set
set.pop()
print(set)
# ********************************* Dictionary**********************************************
mydict = {
    1 : "one",
    2 : "two",
    3 : "Three",
    4 : "Four"
}

# Print the whole Dictionary
print(mydict)

# Print the 1 value of the dictionary:
print(mydict[1])

# print the length of the dictionary
print(len(mydict))

# Print the type
print(type(mydict))

# Change value of dictionary
mydict[1] = "This is One"
print(mydict[1])

# Add item to dictionary
mydict[95] = "Ninety five"
print(mydict)

# Remove specified Item
mydict.pop(95);
print(mydict)


# Print the keys
for i in mydict:
    print(i)
    
#    OR
for x in mydict.keys():
    print(x)
    
# Print the values
for i in mydict:
    print(mydict[i])

#    OR
for x in mydict.values():
    print(x)
    
# Print the Items of the Dictionary
for i in mydict.items():
    print(i)
    
# Clear the dictionary
mydict.clear()
print(mydict)


# ********************************* Functions **********************************************
def prime(n):
    if(n<=1):
        return 0;
    for i in range(2,n):
        if(n%i==0):
            return 0;
    return 1;

x = int(input("Enter a Number : "))
if(prime(x)):
    print(f"The given number {x} is a prime Number")
else:
    print(f"The given number {x} is not a prime Number")
    

def SayHello():
    print("I'm the basic Hello Function")

SayHello()
    
# ********************************* Args ***************************************************
def sum(*args):
    ans = 0
    for i in args:
        ans += i;
    print(ans)

sum(1,2,3,4,5,6)



# ********************************* Qwargs **************************************************
def prinData(**Qwargs):
    for key,value in Qwargs.items() :
        print(f"{key}  is {value}")

prinData(Name = "Lokesh Singh",phone = "7985218361",Email = "lokeshsingh7695@gmail.com")

# ********************************* Exception Handling ****************************************

try:
    print(a)
# except:
except Exception as e:
    print(e)
    print("The variable is Not declared")

# ***************************************** OOPS *********************************************

class student:
    name = ""
    roll = 0
    email = ""
    def set_data(self,name1,email1,roll1):
        self.name = name1;
        self.email = email1;
        self.roll = roll1;
    

karan =  student();
karan.set_data("Karan Saini","karan@gmail.com",78)

print(karan.name)



    