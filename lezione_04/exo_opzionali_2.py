# Esercizio_2:
"""
Guess the Number Game:

    Create a function that generates a random number within a range specified by the user.
    Prompt the user to guess the number within a specified maximum number of attempts.
    Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
    Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.

"""
# Import the 'random' module to generate a random number
import random

# Define a function to play the "guess the number" game
# It takes three arguments: the minimum value, the maximum value, and the number of allowed attempts
def guess_the_number(min_val: int, max_val: int, attempts: int) -> None:
    # Randomly generate a target number between min_val and max_val (inclusive)
    target: int = random.randint(min_val, max_val)

    # Print instructions for the user, including the number range and attempts
    print(f"Guess a number between {min_val} and {max_val}. You have {attempts} attempts.")
    
    # Loop over the number of attempts allowed
    for _ in range(attempts):
        try:
            # Prompt the user for their guess and convert it to an integer
            guess: int = int(input("Your guess: "))
            
            # Check if the guess is lower than the target number
            if guess < target:
                print("Too low.")
            # Check if the guess is higher than the target number
            elif guess > target:
                print("Too high.")
            # If the guess is equal to the target, inform the user and end the game
            else:
                print("Correct! You guessed it!")
                return  # Exit the function if guessed correctly
        except ValueError:
            # Handle the case where the input is not a valid integer
            print("Please enter a valid integer.")
    
    # If the loop ends without a correct guess, reveal the target number
    print(f"Sorry, the number was {target}.")

# Call the function with a range from 3 to 10 and 5 attempts
guess_the_number(3,10,5)