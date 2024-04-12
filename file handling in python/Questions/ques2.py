'''
Write a function in Python to read lines from a text file "notes.txt". Your function should find and display the occurrence of the word "the".

For example: If the content of the file is:
"India is the fastest-growing economy. India is looking for more investments around the globe. The whole world is looking at India as a great market. Most of the Indians can foresee the heights that India is capable of reaching."

The output should be 5
'''

f = open("ques2.txt")
str = f.read()
# Some words may be in upper case, so converting the whole string to lower case
str = str.lower()
ans = str.count("the")
print(ans)
