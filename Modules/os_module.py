# OS Module in Python

import os


if(not os.path.exists("Folder")):
    os.mkdir("Folder")


# Creating Multiple Folder
for i in range(0,100):
    os.mkdir(f"Folder/Day{i+1}")
    


