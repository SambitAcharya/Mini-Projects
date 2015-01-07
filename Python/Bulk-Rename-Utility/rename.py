import os
import random

def getFileList():

    file_list = os.listdir(".")
    return file_list

def removeNumbers(file_list):

    for file_name in file_list:
        numbersremoved = ''.join(i for i in file_name if not i.isdigit())
        os.rename(file_name,numbersremoved)

def removeSymbols(file_list):

    for file_name in file_list:
        symbolsremoved = ''.join(e for e in file_name if (e.isalnum() or e=='.'))
        os.rename(file_name,symbolsremoved)

def removeCharacters(file_list,characters):

    for file_name in file_list:

        index = file_name.find('.')
        ext = file_name[index:]
        name = file_name[:index]
        charactersremoved = ''.join(e for e in name if e not in characters)
        charactersremoved+=ext
        os.rename(file_name,charactersremoved)

def getCharacterSet():

    chars = raw_input("Enter the set of characters. \n")
    char_list = chars.split()
    return char_list

def getSubsitutionWord():

    to_remove = raw_input("Enter the word to substitute. \n")
    to_add    = raw_input("Enter the word to be substituted with. \n")

    return to_add,to_remove

def textSubstitution(file_list,to_add,to_remove):

    for file_name in file_list:

        status = []
        index = file_name.find(to_remove)

        if index == -1:
            status.append(False)
            continue

        end = index+len(to_remove)
        substitute = file_name[:index] + to_add + file_name[end:]
        os.rename(file_name,substitute)

    if not all(status):
        print "The given word was not found in any of the file names."

def main():

    file_list = getFileList()


main()
