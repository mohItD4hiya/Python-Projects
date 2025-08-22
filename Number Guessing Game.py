#Number Guessing Game
import random
number = random.randint(1, 100)
attempts = 0
max_attempts = 7
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("You have 7 attempts to guess it correctly.")
while attempts < max_attempts:
    guess = input(f"Attempt {attempts + 1}: Enter your guess: ")
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)
    attempts += 1
    
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number} in {attempts} attempts!")
        break
    if attempts == max_attempts:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number}. Better luck next time!")
#End of the Number Guessing Game