import random

inputValue, guessValue = random.randint(1, 10), 0
while guessValue != inputValue:
    guessValue = int(input("Guess Number 1 to 9 : "))
print("Well Done")