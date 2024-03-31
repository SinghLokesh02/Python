import webbrowser as wb

channel = input("Enter the Youtube Channel You want to open :- ")
channe_url =  f"https://www.youtube.com/c/{channel}"

wb.open(channe_url)