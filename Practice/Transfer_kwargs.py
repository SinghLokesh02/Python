# Transfer Kwargs Parameter To A Different Function Utilizing Kwargs


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
