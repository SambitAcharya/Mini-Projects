import textwrap

def generateText(text):

    num = 1
    den = len(text)/140 + 1
    add = str(num)+'/'+str(den)+': '
    start = 0
    const = 140 - len(add)
    end = start + const
    count = 0

    while count < den:
        add = str(num)+'/'+str(den)+': '
        tweet = add + text[start:end]
        print tweet + "\n"
        print len(tweet)
        start=end+1
        end = start + const
        count+=1
        num+=1

def generateImage():
    return 0

def getText():
    return raw_input("Enter Your Tweet.\n")

def main():

    text = getText()
    generateText(text)

main()
