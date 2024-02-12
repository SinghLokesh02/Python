# Guess the Number Game
import random
import time

print("\n\nWelcome to the Guess the Number Game")
time.sleep(2)

# Generating a random Number between 1 - 100
guess = round(random.random() * 100)

data = 0
count = 0
while data != guess:
    data = int(input("\nEnter Your Number between 1 - 100 : "))
    if guess < data:
        print("You guess is higher")
    elif guess > data:
        print("Your guess is lower")
    count += 1

print(f"\nYou Guessed it right ✅✅ in {count} Attempt\n")
