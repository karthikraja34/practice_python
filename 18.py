# Cows And Bulls 

""" 
Create a program that will play the 'cows and bulls' game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a 'cow'. For every digit the user guessed correctly in the wrong place is a 'bull.'' Every time the user makes a guess, tell them how many 'cows' and 'bulls' they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:

  Welcome to the Cows and Bulls Game! 
  Enter a number: 
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...
Until the user guesses the number.
"""

import random


li2 = []

def gen():
    li = list()
    while(len(li)<4):
        li.append(random.randint(0,9))  
    return li

def user():
    num = int(raw_input("Enter the number : "))
    li2 = [int(i) for i in str(num)]
    # print li2
    return li2

def main():
    a = gen()
    stra = ''.join(str(e) for e in a)
    # print int(stra)
    b = [0]
    strb = ''.join(str(e) for e in b)
    while(int(stra) != int(strb)):
        b = user()
        strb = ''.join(str(e) for e in b)
        i = 0
        cows = 0
        bulls = 0
        for x in a:
            if x in b:
                if x is b[i]:
                    cows += 1
                if x is not b[i]:
                    bulls += 1
            i += 1
        print "%d cows , %d bulls "% (cows,bulls)

    print "yay!!! You Won the Game "

main()