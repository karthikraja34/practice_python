# String Lists

""" 
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
 """

def palindrome(a):
    l = 0
    r = len(a)-1
    while (l<r):
        if(a[l] != a[r]):
            return False
        l+=1
        r-=1
    return True

print palindrome("madam")

word = raw_input("Enter a word : ")

if(word.lower() == word[::-1].lower()):
    print "It is a palindrome"
else:
    print "It is not a palindrome"