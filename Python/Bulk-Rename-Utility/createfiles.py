import random

def createFiles():

    for i in range(100):

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        filename = ""

        for j in range(10):
            next_letter_index = random.randrange(len(alphabet))
            filename = filename + alphabet[next_letter_index]

        filename = replaceWithNumber(filename)
        filename = replaceWithUppercaseLetter(filename)
        filename = replaceWithSymbol(filename)

        a = open(filename+'.txt','w')
        a.close()

def replaceWithNumber(fname):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(fname)//2)
        fname = fname[0:replace_index] + str(random.randrange(10)) + fname[replace_index+1:]
        return fname

# Function to replace 1 or 2 letters with an uppercase letter
def replaceWithUppercaseLetter(fname):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(fname)//2,len(fname))
        fname = fname[0:replace_index] + fname[replace_index].upper() + fname[replace_index+1:]
        return fname

def replaceWithSymbol(fname):
    symbols = "~!@#$%^&*'?><}+=_-'"
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(fname)//2,len(fname))
        fname = fname[0:replace_index] + symbols[random.randrange(len(symbols))] + fname[replace_index+1:]
    return fname

def main():
    createFiles()

main()
