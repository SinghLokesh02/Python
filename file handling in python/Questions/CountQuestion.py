# Count the Number of Word, line, vowel and space characters in a file

def CountVowel(str):
    count = 0
    vowels = 'aeiouAEIOU'
    for data in str:
        if(data in vowels):
            count += 1
    return count
 

f = open("ques2.txt")
count = 0
word = 0
vowel = 0
space = 0
for data in f:
    print(data,end="")
    space += data.count(" ")
    lst = data.split(" ")
    for data in lst: # word by word
        vowel += CountVowel(data)
    word += len(lst)
    count += 1
    
# word, vowel, spaace, line
print(f"\nThe lines in the text file is {count} lines")
print(f"The words in the text file is {word} words")
print(f"The vowels in the text file is {vowel} Vowels")
print(f"The Space in the text file is {space} Space")
    
    



# Count the number of lines

# f = open("Text.txt", "r")
# ans = f.readlines() # Readlines() returns a list of lines
# print(ans)
# print(len(ans))