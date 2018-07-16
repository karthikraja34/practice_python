# Odd Or Even

""" 
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
"""


""" 
If the number is a multiple of 4, print out a different message.
"""
 

num = int(raw_input("Enter a number : "))
if (num % 4) == 0 :
    print "It is a multiple of 4"
elif (num % 2)==0:
    print "It is an even number"
else:
    print "It is a Odd number"

""" 
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

num = int(raw_input("Enter a number : "))
check = int(raw_input("Enter the divisor : "))

if((num % check) == 0):
     print "It is getting divided"
else:
     print "It is not getting divided"

