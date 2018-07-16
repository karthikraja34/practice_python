# List Overlap

""" 
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
 """

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]



print list(set(a) & set(b))
""" 
Randomly generate two lists to test this
 """

import random

a=[]
b=[]

for i in range(1,random.randint(1,30)):
    a.append(random.randint(1,100))

for i in range(1,random.randint(1,30)):
    b.append(random.randint(1,100))
print a,b

""" 
Write this in one line of Python (don't worry if you can't figure this out at this point - we'll get to it soon)
 """

rand_list = [random.randint(1, 100) for _ in range(1,random.randint(1,50))]
print rand_list