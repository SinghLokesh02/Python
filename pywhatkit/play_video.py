# Play a YouTube video.

import pywhatkit as pyk

search_input = input("Enter the thing You want to search for :- ")
try:
    pyk.playonyt(search_input)
    print("Searching...")
except Exception as e:
    print("Some Error Occured during search")
    
print("The Program Has been Over Now 😃👍")