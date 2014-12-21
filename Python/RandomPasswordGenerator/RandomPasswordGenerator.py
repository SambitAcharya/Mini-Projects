#Imports
import random

#FUNCTIONS

#Function to generate the passwords
def generatePassword(pw_length):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    passwords = [] # List to store all the passwords

    for i in pw_length:
        
        password = "" #Variable to store the generated password
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]
        
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        
        passwords.append(password) # Appending the generated password to the master list
    
    return passwords

# Function to replace 1 or 2 characters with a number
def replaceWithNumber(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
        return pword

# Function to replace 1 or 2 letters with an uppercase letter
def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2,len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
        return pword


# main fuction
def main():
    
    numPasswords = int(input("How many passwords do you want to generate? "))
    
    print("System is about to generate " +str(numPasswords)+" passwords")
    
    passwordLengths = []

    print("Enter the length of the passwords. Minumum Length = 3")

    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        if length<3:
            length = 3
        passwordLengths.append(length)
    
    
    Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print ("Password #"+str(i+1)+" = " + Password[i])


# RUN THE CODE
main()