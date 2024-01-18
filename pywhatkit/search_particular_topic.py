# Search Particular topic

import pywhatkit as pyk

search_input = input("Enter the thing You want to search for :- ")
try:
    print("Searching...")
    pyk.info(search_input,lines = 4)
except Exception as e:
    print("Some Error Occured during search")
    
print("The Program Has been Over Now !!")