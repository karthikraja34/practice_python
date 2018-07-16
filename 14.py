# List Remove Duplicates


""" Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates. """

""" Write two different functions to do this - one using a loop and constructing a list, and another using sets. """

li = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ,5 ,8]

print list(set(li))
y = []

for x in li:
    if x not in y:
        y.append(x)
print y