import operator

def clean_up_list(word_list):

    clean_word_list = []
    for word in word_list:
        word = ''.join(e for e in word if e.isalnum())
        if len(word)>0:
            clean_word_list.append(word)
    return(clean_word_list)

def create_dictionary(clean_list):

    word_count = {}
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key,value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key,value)

def countPhrases(content,number_of_phrases):

    word_list = []
    words = content.lower().split()

    for each_word in words:
        word_list.append(each_word)

    clean_list = clean_up_list(word_list)
    create_dictionary(clean_list)

def main():

    content = input("Enter the paragraph for phrase counting \n")
#    number_of_phrases = int(input("Enter the length of each phrase \n"))
    number_of_phrases = 1
    '''
    while number_of_phrases < 0 or number_of_phrases > 5:
        print("Number Of Phrases can only be between 1 to 5 \n")
        number_of_phrases = int(input("Enter the length of each phrase \n"))
    '''
    countPhrases(content,number_of_phrases)

main()
