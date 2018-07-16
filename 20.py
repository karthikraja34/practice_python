# Element Search

""" 
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.


"""
import random

li = [random.randint(0,100) for x in range(10)]
li = sorted(li)

print li

num = int(raw_input("Enter the number : "))

if num in li:
    print "Yes"
else:
    print "NO"

""" Use binary search. """


def binarySearch(alist, item):
	    if len(alist) == 0:
	        return False
	    else:
	        midpoint = len(alist)//2
	        if alist[midpoint]==item:
	          return True
	        else:
	          if item<alist[midpoint]:
	            return binarySearch(alist[:midpoint],item)
	          else:
	            return binarySearch(alist[midpoint+1:],item)
	
print(binarySearch(li, num))
# print(binarySearch(testl, 13))


# print bin()
