'''
Write a function in python to count the number of lines from a text file "story.txt" which is not starting with an alphabet "T". 

Example: If the file "story.txt" contains the following lines:
A boy is playing there.
There is a playground.
An aeroplane is in the sky.
The sky is pink.
Alphabets and numbers are allowed in the password.
The function should display the output as 3 
'''
def count_lines():
    f = open("story.txt")
    count = 0
    for line in f:
        if line[0] != "T":
            count += 1
    print(count)

# Count the number of lines from the file "story.txt" which is not starting with an alphabet "T"
count_lines()

# Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.

def display_words():
    file = open("story.txt")
    count = 0
    for line in file:
        word = line.split(" ")
        for single in word:
            if(len(single)<4):
                count += 1
    print(f"The Number of Words which have length less then 4 is {count}")

display_words()



# Write a function in Python to count and display the total number of words in a text file.
def count_words():
    file = open("story.txt")
    count = 0
    for line in file:
        word = line.split(" ")
        count += len(word)
    print(f"The Number of Words in the file is {count}")

count_words()



