# Transfer Kwargs Parameter To A Different Function Utilizing Kwargs

# Method - 1) Using Direct Transfer


def function1(**kwargs):
    print("The kwargs before changing the value: ")
    for key, value in kwargs.items():
        print(key, value)

    # Chnaging the value of kwargs
    kwargs["name"] = "Bran Stark"
    function2(**kwargs)


def function2(**kwargs):
    print("\nThe kwargs before After the value: ")
    for key, value in kwargs.items():
        print(key, value)


function1(name="John", age=25, roll_no=101, number=9898956422)

# Using Dictionary Unpacking


def Change_Data(mydict):
    mydict["Age"] = 22
    Print_Data(**mydict)


def Print_Data(name=None, Age=None, Role=None, email=None):
    print(f"The name is {name}")
    print(f"The Age is {Age}")
    print(f"The Email is {email}")
    print(f"The Role is {Role}")


my_dict = {
    "name": "Lokesh Singh",
    "email": "lokeshsingh7695@gmail.com",
    "Role": "Software Trainer",
    "Age": 25,
}

Change_Data(my_dict)


# Using Unpacking with **kwargs:

def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"The {key} is : {value}")

def greeting(**kwargs):
    greet(**kwargs)

greeting(name="Lokesh Singh", age=22, city="Gwalior")

# Using Passing Explicitly:

def Change_kwargs(**kwargs):
    name = kwargs["name"]
    email = kwargs["email"]
    phone = kwargs["phone"]
    return Return_data(name,email,phone)

def Return_data(name,email,phone): 
    return {"name":name,"email":email,"phone":phone}
    
    
ans = Change_kwargs(name = "Lokesh Singh",email='lokeshrandom@gmail.com',phone="1234567890")

print(ans)
