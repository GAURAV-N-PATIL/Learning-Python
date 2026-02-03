# Game for Guessing a Number
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
import random
from unittest import case
number_to_guess = random.randint(1, 100)
attempts = 0
print("Choose a difficulty. Type 'easy' or 'hard':")
print("easy: Unlimited attempts---Choice : 1")
print("Difficult: 10 attempts---choice : 2")
User_choice=int(input("Enter Your Choice EASY(1) or DIFFICULT(2):"))
match User_choice:     # switch  case of python
    case 1:
        print("You have unlimited attempts to guess the number.")
        print("Guess the Number:")
        while (User_choice == 1):        # while loop for unlimited attempts
            User_Guess=int(input("Guess:"))
            attempts += 1
            if(User_Guess < number_to_guess):
                print("Too low. Guess again.")
            elif(User_Guess > number_to_guess):
                print("Too high. Guess again.")
            else:
                print("You Guessed the number in", attempts, "attempts! Congratulations!")
                exit()
            
    case 2:
        print("You have 10 attempts to guess the number.")
        for attempt in range(1, 11):     # for loop for 10 attempts
            User_Guess=int(input("Guess the Number:"))
            if(User_Guess < number_to_guess):
                print("Too low. Guess again.")
            elif(User_Guess > number_to_guess):
                print("Too high. Guess again.")
            else:
                print("You Guessed the number in", attempt, "attempts! Congratulations!")
                break
    case _:
        print("Invalid choice. Please restart the game and choose either 1 or 2.")
        exit()

