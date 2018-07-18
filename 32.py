
import random




print "Welcome to Hangman!"
secret_word=choose_random_word()
dashes=list(secret_word)
display_list=[]
for i in dashes:
    display_list.append("_")
count=len(secret_word)
guesses=0
letter = 0
used_list=[]
while count != 0 and letter != "exit":
    print " ".join(display_list)
    letter=input("Guess your letter: ")

    if letter.upper() in used_list:
        print "Oops! Already guessed that letter."
    else:
        for i in range(0,len(secret_word)):
            if letter.upper() == secret_word[i]:
                display_list[i]=letter.upper()
                count -= 1
        guesses +=1
    used_list.append(letter.upper())

if letter == "exit":
    print "Thanks!"
else:
    print " ".join(display_list)
    print "Good job! You figured that the word is "+secret_word+" after guessing %s letters!" % guesses




def choose_random_word():
    fi =file("hangman.txt","r")
    lines = fi.readlines()
    fi.close()
    return lines[random.randint(0,len(lines)-1).strip()
