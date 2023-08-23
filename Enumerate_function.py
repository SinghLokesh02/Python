# Enumerate Function in Python

# The enumerate() function adds a counter to an iterable.
# So for each element in cursor, a tuple is produced with (counter, element);
# the for loop binds that to row_number and row, respectively.

marks = [90, 25, 67, 45, 80]
index = 0
for number in marks:
    print(number)
    if(index == 2):
        print("Congratulations you have got 3rd position")
    index += 1


# Enumerate function
print("\n\nUsing Enumerate function\n")
for index, number in enumerate(marks):
    print(number)
    if(index == 2):
        print("Congratulations you have got 3rd position")
    index += 1