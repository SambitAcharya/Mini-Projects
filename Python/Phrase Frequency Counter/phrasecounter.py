'''

Created For Mini Projects Repository

Problem: Design a Phrase Frequency Counter.

Implementation: The code counts the number of times different phrases occur in
a given paragraph(given by the user). The user has to choose how many words a
phrase would contain and then the code would display all the possible phrases
of that many words and their counts. All the measures have been taken to ensure
that the program is bug free.

@author: Sambit

'''

#Imports
import operator

#Functions

#Function to create the phraselist based on the user input
def createPhraseList(clean_list,number_of_phrases):

    '''

        @param Input: List without special symbols and the number of phrases
        @return Output: List containing all the phrases of @number_of_phrases length.

    '''

    phrase_list = []
    phrase = ''
    count = 0
    max_count = len(clean_list) - number_of_phrases + 1

    while count<max_count:
        for i in range(number_of_phrases):
            phrase = phrase + clean_list[count+i] + " "
        phrase_list.append(phrase)
        phrase = ''
        count+=1

    return(phrase_list)

#Function to create the dictionary which would store all the phrases and their counts.
def createDictionary(phrase_list):

    '''

        @param Input: List containing all the phrases.
        @return Output: Dictionary containing all the phrases and their counts.

    '''

    phrase_count = {}

    for phrase in phrase_list:
        if phrase in phrase_count:
            phrase_count[phrase] += 1
        else:
            phrase_count[phrase] = 1

    return phrase_count

#Function to clean up the list from special symbols so as to allow only alphanumeric characters.
def cleanUpList(word_list):

    '''

        @param Input: List containing all the words.
        @return Output: @param List devoid of special symbols

    '''

    clean_word_list = []

    for word in word_list:
        word = ''.join(e for e in word if e.isalnum())
        if len(word)>0:
            clean_word_list.append(word)

    return(clean_word_list)

#Function to get input from the user, split them into words and pass on for further processing.
def getWords(content):

    '''

        @param Input: String containing users input.
        @return Output: Symbol free list and the length of the list made from @param string

    '''

    word_list = []
    words = content.lower().split()

    for each_word in words:
        word_list.append(each_word)

    clean_list = cleanUpList(word_list)
    length_of_content = len(clean_list)

    return clean_list,length_of_content

#Function to count all the phrases
def countPhrases(clean_list,number_of_phrases):

    '''

        @param Input: A clean list and the number of phrases given by the user.
        @return Output: Dictionary containing the phrase count.

    '''

    phrase_list = createPhraseList(clean_list,number_of_phrases)
    phrase_count = createDictionary(phrase_list)

    return phrase_count

#Main Function
def main():

    condition = False

    while not condition:

        content = input("Enter the paragraph for phrase counting \n")
        number_of_phrases = int(input("Enter the length of each phrase \n"))

        while number_of_phrases < 0 :
            print("Number Of Phrases can only be positive \n")
            number_of_phrases = int(input("Enter the length of each phrase \n"))

        clean_list,length_of_content = getWords(content)
        condition = length_of_content - number_of_phrases

        if condition < 0:
            condition = False

        if not condition:
            print("Error")
            print("Length of content is less than the length of phrase.")
            print("Input again.")

    phrase_count = countPhrases(clean_list,number_of_phrases)

    #Sorting the dictionary in increasing order of values.
    for key,value in sorted(phrase_count.items(), key=operator.itemgetter(1)):
         print(key,value)

main()
