# Max Of Three 

""" Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!

 """

a,b,c = raw_input("Enter 3 numbers separated by space : ").split()
a,b,c = int(a),int(b),int(c)


if (a >= b) and (a >= c):
    largest = a

elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c
        
print largest