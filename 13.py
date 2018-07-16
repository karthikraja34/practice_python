# Fibonacci

""" 
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate
 """

a = -1
b = 1

limit = int(raw_input("Enter the number : "))

for i in range(1,limit+1):
    c = a+b
    a = b
    b = c
    print c