'''

Created for Mini-Projects Repository

Problem: A xkcd password generator

Implementation: Four random words are picked out of a file of 20 words and concantinated
to make a password. Surprisingly, this password is stronger than the other password generator in the
folder.

@author: Sambit

'''

#Imports
import random

#Reading words from a file
words = open("words.txt",'r').readlines()
words = [word.replace("\n","") for word in words]

#List to store the random password generated
pwlist = []

#Choosing four random words and putting them in a list
for i in range(4):
    randWord = words[random.randrange(len(words))]
    pwlist.append(randWord)

#Creating the password from the list created
password =  ''.join(i for i in pwlist)

#Printing the password to the console
print password
