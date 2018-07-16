# List Ends

""" 
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
 """

a =[5, 10, 15, 20, 25]
import random

def random_list():
    li = list(random.sample(range(50),random.randint(0,25)))
    print "Random list is {}".format(li)
    return li

def genList(li):
    list1 = [li[0],li[-1]]
    return list1

x = genList(random_list())
print(x)