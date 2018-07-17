# File Overlap 

""" Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can't be divided by any other number. And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.) """

fp = file('primenumbers.txt','r')
read = fp.read()
fp.close()
li = read.split("\n")

fp2 = file('happynumbers.txt','r')
read2 = fp2.read()
fp2.close()
li2 = read2.split("\n")

ans = [x for x in li if x in li2]
print ans