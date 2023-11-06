# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
# import Alice_spellCheck.Search_types as Search_types
import Search_types
import time

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("Alice_spellCheck\data-files\dictionary.txt")
    aliceWords = loadWordsFromFile("Alice_spellCheck\data-files\AliceInWonderLand.txt")
    loop = True
    while loop:
        #python print menu
        print("\nMAIN MENU")
        print("1: Spell Check a Word")
        print("2: Spell Check Alice In Wonderland")
        print("4: EXIT")

        # Get Menu Selection from User

        selection = input("Enter Selection (1-4): ")


        # Take Action Based on Menu Selection

        if selection == "1":
            spell_check_word(dictionary)
        elif selection == "2":
            spell_check_text(aliceWords,dictionary)
        elif selection == "3":
            print("\nOption 3")
        elif selection == "4":
            print("\nEXIT")
            loop = False



    
    # Print first 50 values of each list to verify contents
    # print(dictionary[0:50])
    # print(aliceWords[0:50])
# end main()

def spell_check_word(dictionary):
    word = input("search for: ")
    LorB = input("linear or binary (l/b)")
    start_time = time.time()
    found = search(dictionary,word,LorB)
    end_time = time.time()
    total = end_time - start_time
    if found == -1:
        print(f"{word} not found in dictionary. ({total} seconds)")
    else:
        print(f"{dictionary[found]} is IN the dictionary at position {found}. ({total} seconds) ")


def search(array,item,LorB):
    if LorB == "l":
        found = Search_types.linearsearch(array,item)
        return found
    else:
        found = Search_types.binarySearch(array,item)
        return found

def spell_check_text(words,dictionary):
    LorB = input("linear or binary (l/b)")
    words = [x.lower() for x in words]
    not_found = 0
    start_time = time.time()
    for word in words:
        test = search(dictionary,word,LorB)
        if test == -1:
            not_found +=1
    end_time = time.time()
    total = end_time - start_time
    print(f"Number of words NOT found in dictionary: {not_found}. ({total} seconds)")



def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()
