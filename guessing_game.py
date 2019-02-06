"""Command line guessing game."""
import random

#VARIABLES
num_guesses = 0
guesses = []
player_guess = 11
num = random.randint(0,10) #Generate number to guess
player_name = input("What is your name? ") #Get player name

#instructions
print("Hello " + player_name + ", here is how the game works:")
print("You will have only 7 tries to guess a number between 0 and 10. ")
print("Good Luck!")

#while loop
while num_guesses < 7 and player_guess != num:
    player_guess = int(input("Input your guess: "))
    guesses.append(player_guess)
    num_guesses += 1

#conditionals
#win
if player_guess == num:
    print(player_name + ", you Won!!")
    print("It took you", num_guesses,"guesses to win!")
    print("These were your guesses:")
    print(guesses)
#lose
else:
    print(player_name + ", you have used up all of your guesses!")
    print("These were the numbers that you guessed:")
    print(guesses)
    print("This was the correct number: ", num)

