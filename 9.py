# Guessing Game One

""" 
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
 """

""" 
 Keep the game going until the user types 'exit'
Keep track of how many guesses the user has taken, and when the game ends, print this out.
  """
import random

num = random.randint(1,9)
guess = 0
while True:
    input1 = (raw_input("Enter a number or press 'Exit' : "))
    if(input1 == "Exit"):
        break
    n = int(input1)
    if(n == num):
        print " you win in %d guesses" % guess
        num = random.randint(1,9)
    elif (n > num):
        print "High"
    elif (n < num):
        print "Low"
    guess+=1
