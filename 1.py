# Character Input

""" 
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

"""


name = raw_input("Enter your name : ")
age  = int(raw_input("Enter your age : "))

print "%s will turn 100 years old in %d" % (name,(2018 + 100 - age))

""" 
Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.

Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""
num = int(raw_input("Enter number of times to print : "))
ans =  "%s will turn 100 years old in %d \n" % (name,(2018 + 100 - age))

print ans * num