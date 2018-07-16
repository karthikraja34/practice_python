# Password Generator

""" Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method. """
import random

def passwordGenerator():
    charsUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    charsLow = "abcdefghijklmnopqrstuvwxyz"
    charsNumber = "0123456789"
    charsSpecial = "!@#$%&*()[]{}"
    password = ''
    password += random.choice(charsUpper)
    password += random.choice(charsLow)
    password += random.choice(charsNumber)
    password += random.choice(charsSpecial)
    password += random.choice(charsUpper)
    password += random.choice(charsLow)
    password += random.choice(charsNumber)
    password += random.choice(charsSpecial)
    return password

print passwordGenerator()

""" Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list. """

qstn = raw_input("Do you want weak password ? (yes or no) ")
if (qstn == "yes"):
    weak = ["password","hellohello","strongpassword"]
    print random.choice(weak)
else:
    print passwordGenerator()
