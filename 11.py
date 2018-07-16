# Check Primality Functions

""" 
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
 """
import math

def isPrime(num):
    if(num == 2):
        return True
    if(num == 1):
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if((num % i) ==0):
            return False
    return True

if(isPrime(1)):
    print "It is prime number"
else:
    print "Not a Prime"