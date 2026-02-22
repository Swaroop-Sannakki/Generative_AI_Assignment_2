# #Q16 Create a number guessing game where the computer picks a random number between 1-100 and the user gets 7 attempts. 
# Rules: 
# 1. After each guess, show if guess is too high or too low and attempts remaining 
# 2. If correct: congratulate and show attempts used 
# 3. If failed: reveal the number 
# 4. Ask to play again

import random  # Import random module to generate random numbers

best_score = None  # Store best (minimum) attempts used across games initially as none 

while True:  #  outer while loop is applied so the game can repeat (i.e play again)
    num = random.randint(1, 100)  # chooses a random number between 1 and 100 and store it in num variable
    attempts_left = 7             # it defines Player has 7 attempts
    attempts_used = 0             # Count how many guesses the player used initially defined to zero

    print("\nGuess the number (1–100). You have 7 attempts.")  # print the game message

    while attempts_left > 0:  # Loop while player still has attempts
        guess = int(input("Enter guess: "))  # Take player's guess as an input 
        attempts_left -= 1                  # Decrease attempts remaining
        attempts_used += 1                  # Increase attempts used count

        if guess == num:  # If guess equals the secret number
            print(f" Congratulations!!.. You guessed in {attempts_used} attempts.")  # print Success message for user 

            # Check if this is the best score so far or not using if else condition 
            if best_score is None or attempts_used < best_score:
                best_score = attempts_used  # Update the best score
                print("New best score!")  # Show best score message

            break  # Exit guessing loop because player won

        elif guess < num:  # If guess is smaller than number
            if abs(num - guess) <= 5:  # If guess is within 5 of number
                print(f" Too low ( you are very close!). Attempts left: {attempts_left}")
            else:
                print(f" Too low. Attempts left: {attempts_left}")

        else:  # If guess is greater than number
            if abs(num - guess) <= 5:  # If guess is within 5
                print(f" Too high (you are very close!). Attempts left: {attempts_left}")
            else:
                print(f"Too high. Attempts left: {attempts_left}")

    else:  # This runs if loop ends without break (player failed)
        print(f" Out of attempts! The number was {num}")  # Reveal number

    if best_score is not None:  # If at least one game was won
        print("Best score:", best_score, "attempts")  # Show best score

    again = input("Play again? (yes/no): ").lower()  # Ask user if they want to play again
    if again != "yes":  # If user does not type y
        print("Thanks for playing!")  # Exit message
        break  # Stop outer loop to end game
    
#Multiple outputs tested
# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q16_Number_Guessing_Game.py

# Guess the number (1–100). You have 7 attempts.
# Enter guess: 55
# Too high. Attempts left: 6
# Enter guess: 40
# Too high. Attempts left: 5
# Enter guess: 30
#  Too high (you are very close!). Attempts left: 4
# Enter guess: 26
#  Too high (you are very close!). Attempts left: 3
# Enter guess: 24
#  Too low ( you are very close!). Attempts left: 2
# Enter guess: 22
#  Too low ( you are very close!). Attempts left: 1
# Enter guess: 25
#  Congratulations!!.. You guessed in 7 attempts.
# New best score!
# Best score: 7 attempts
# Play again? (yes/no): yes

# Guess the number (1–100). You have 7 attempts.
# Enter guess: 34
# Too high. Attempts left: 6
# Enter guess: 24
# Too high. Attempts left: 5
# Enter guess: 14
#  Too low ( you are very close!). Attempts left: 4
# Enter guess: 19
#  Too high (you are very close!). Attempts left: 3
# Enter guess: 15
#  Congratulations!!.. You guessed in 5 attempts.
# New best score!
# Best score: 5 attempts
# Play again? (yes/no): yes

# Guess the number (1–100). You have 7 attempts.
# Enter guess: 90
# Too high. Attempts left: 6
# Enter guess: 80
# Too high. Attempts left: 5
# Enter guess: 70
# Too high. Attempts left: 4
# Enter guess: 60
# Too high. Attempts left: 3
# Enter guess: 50
# Too high. Attempts left: 2
# Enter guess: 40
# Too high. Attempts left: 1
# Enter guess: 30
# Too high. Attempts left: 0
#  Out of attempts! The number was 5
# Best score: 5 attempts
# Play again? (yes/no): no
# Thanks for playing!

