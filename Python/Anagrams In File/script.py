# The function should return a data structure which maps each word in
# the word list to a list of all anagrams of that word which are
# also valid words in the /tmp/dict file

def getWordsFromFile(loc):

    '''

        Function to get all the words from the file separated by a new line

    '''

    with open(loc) as f:
        words = f.read().split('\n')
        words.pop()
    return words

def formSortedWord(char_list):

    '''

        Function to form a word by sorting a list of character in increasing order

    '''

    word = ''.join([char for char in sorted(char_list)])
    return word

def sortWords(word_list):

    '''

        Function to create a list of words after sorting the characters
        in increasing order.

    '''

    sorted_words = []
    for word in word_list:
        sorted_words.append(formSortedWord(word))
    return sorted_words

def createAnagramDictionary(word_list, file_word_list):

    '''

        Function to create the dictionary with the words in the list
        as the key and a list of words which are its anagrams and are
        present in the file.

    '''

    sorted_word_list = sortWords(file_word_list)
    anagram_dict = {}

    for word in word_list:
        sorted_word = formSortedWord(word)
        list_of_words = [file_word_list[index] for index,each_word in enumerate(sorted_word_list) if each_word == sorted_word]
        anagram_dict[word] = list_of_words

    return anagram_dict

def main():

    # List of words in the given input
    word_list = ['radio','active', 'file','generation','waking', 'up', 'Hackerearth']

    file_word_list   = getWordsFromFile('tmp/dict/words.txt')
    anagram_dict = createAnagramDictionary(word_list, file_word_list)

    print anagram_dict

if __name__ == '__main__':
    main()
