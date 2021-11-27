import random
title="Number Guessing Game"
print(title)
number=random.randint(1,100)
guess="guess the number I am thinking of (1-100)"
print(guess)
chances=0

while (chances<6):
    intro=int(input("Enter your guess:-"))
    if (intro == number):
        print("congrats! you got it right")
        break
    elif (intro>number):
        print("Your guess was too high! try again")
    else :
        print("Your guess was too low! try again")
   
    chances=chances+1    
if not (chances<6):
    print("you lose!!! The number is:", number)

