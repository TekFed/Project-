#install Pydictionary to get all the words 

from PyDictionary import PyDictionary

dictionary = PyDictionary()

nav = input("Do you wish to sear for \"a word\" or \"group of words\": ")

def a_word():
    word = input("Enter a word: ")

    if word == "":
        quit()

    print(dictionary.meaning(word))

def group_words():
    words = input("Enter the words: ")

    if words == "":
        quit()

    print(dictionary.printMeanings(words)) #getMeanings to retuen it in a python dictionary format


if nav == "A WORD".lower():
    a_word()
elif nav == "A GROUP OF WORDS".lower():
    group_words()
else:
    print('Wrong option.')
    quit()




