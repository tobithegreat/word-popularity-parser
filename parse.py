import re
from operator import itemgetter
import sys

file = sys.argv[1]
try:
    f = open(file, "r")
except IOError:
    print "Cannot locate that file in the directory. Please try again."
    sys.exit()
data = f.read()
f.close()

popular_words = None


def choice():
    choice = raw_input("Please enter P to view the most popular words in your file in descending order. Enter M to view the most popular word of a specific number of characters. Enter Q to quit: ").strip()
    
    if choice.upper() == "P":
        get_popular_words(data)
    elif choice.upper() == "M":
        most_common_word(data)
    elif choice.upper() == "Q":
        sys.exit()



def get_popular_words(data):
   # Iterate across all whole words in the file
    wordcount = {}
    new_words = []
    for word in data.split():
        # Check to add words to list if not already
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    num = int(raw_input("How many words would you like to view? "))
    length = int(raw_input("What is the word length cutoff? "))
    wordcount = sorted(wordcount.items(), key = itemgetter(1), reverse = True)
    global popular_words
    popular_words = wordcount
    for inst, (word, number) in enumerate(wordcount):
        if len(word) >= length:
            new_words.append(wordcount[inst])
    wordcount = new_words[:num]
    for k,v in wordcount:
      print("{} appears {} times".format(k, v))
    choice()

def most_common_word(words):
    word_length = int(raw_input("What number of characters would you like to search for? "))
    word = None
    new_words = []
    for inst, (word, number) in enumerate(words):
        if len(word) == word_length:
            new_words.append(word)
    try:
        print("The most common word at this word length is: {}". format(new_words[0]))
    except IndexError:
        print("There are no words at this word length in the data.")

    choice()

if __name__ == '__main__':
    choice()


