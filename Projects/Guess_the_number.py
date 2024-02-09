# Guess the Number Game
import random

# Generating a random Number between 1 - 100
guess = round(random.random() * 100)

data = 0
count = 0
while data != guess:
    data = int(input("Enter Your Number : "))
    if guess < data:
        print("You guess is higher")
    elif guess > data:
        print("Your guess is lower")
    count += 1

print(f"You Guessed it right ✅✅ in {count} Attempt")
