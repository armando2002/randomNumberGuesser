# random number guesser
# Programming Fundamentals Assessment 1

import random

while True:
    start = input("Enter the start of the range: ")
    if start.isdigit() == True:
        break
    else:
        print("Please enter a valid number.")
while True:
    end = input("Enter the end of the range: ")
    if end.isdigit() == True:
        break
    else:
        print("Please enter a valid number.")

random_number = random.randrange(int(start), int(end))
guesses = 0
guess = None

while guess != random_number:
    inputguess = input("Guess a number: ")

    if inputguess.isdigit() == False:
        print("Please enter a valid number.")
        continue
    else:
        guesses += 1
        guess = int(inputguess)
        continue

if guesses == 1:
    print(f"You guessed the number in {guesses} attempt")
else:
    print(f"You guessed the number in {guesses} attempts")

