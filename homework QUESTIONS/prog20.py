### PRACTICAL FOR XI CS - 2020-21 #
# 20.	Write a program for number guessing game and
#       give 7 chance to guess the randomly generate
#       number between 1,100


import random
import math

lower = int(input("Emter Lower bound:- ")) # Taking Inputs
upper = int(input("Enter Upper bound:- "))  # Taking Inputs

                                        # generating random number between
                                        # the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n")

                                        # Initializing the number of guesses.
count = 0

                                        # for calculation of minimum number of
                                        # guesses depends upon range
while count < math.log(upper - lower + 1, 2):
        count += 1                                  
        guess = int(input("Guess a number:- "))  # taking guessing number as input
        if x == guess:                          # Condition testing
                print("Congratulations you did it in ", count, " try")
                break
                # Once guessed, loop will break 
        elif x > guess:
                print("You guessed too small!")
        elif x < guess:
                print("You Guessed too high!")
# If Guessing is more than required guesses, # shows this output.
if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d"%x)
        print("\tBetter Luck Next time!")
# Better to use This source Code on pycharm!
