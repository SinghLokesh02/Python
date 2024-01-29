# Method - 1 Using Direct method

tuple1 = (1, 2)
tuple2 = ("One", 67)
tuple3 = (1, 5, 3, 9)

set_of_tuples = {tuple1, tuple2, tuple3}
print("The set of tuples is")
print(set_of_tuples)


# Method - 2 Using set() method

tuple1 = (1, 2)
tuple2 = ("One", 67)
tuple3 = (1, 5, 3, 9)

# Creating a list of tuple
tuple_list = [tuple1,tuple2,tuple3]

set_of_tuples = set(tuple_list)
print("The set of tuples is")
print(set_of_tuples)


# Method - 3 Using add() method of set

tuple1 = (1, 2)
tuple2 = ("One", 67)
tuple3 = (1, 5, 3, 9)

# Creating a list of tuple
set_of_tuples =  set()

# Adding Tuples one by one
set_of_tuples.add(tuple1)
set_of_tuples.add(tuple2)
set_of_tuples.add(tuple3)
 
print("The set of tuples is")
print(set_of_tuples)
