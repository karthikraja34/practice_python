# Read From File

""" Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it! """

fp = file('nameslist.txt','r')
read = fp.read()
fp.close()
li = read.split('\n')
# print li
names = {}

for i in li:
    if i not in names:
        names[i] = 1
    else:
        names[i] += 1
print names

""" Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each 'category' of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you're going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post. """
fp = file('nameslist2.txt','r')
read = fp.read()
fp.close()

li = read.split("\n")
names = {}

for i in li:
    if i not in names:
        names[i[-24:-4]] = 1
    else:
        names[i[-24:-4]] += 1
print names