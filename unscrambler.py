import itertools

allWords = set()

def init():
    for line in open("2of12inf.txt"):
        allWords.add(line.strip())

permutations = itertools.permutations("dictionayr")

# Given a series of letters, returns all permutations that are present in Alan
# Beale's 2of12inf list (part of the 12dicts dictionaries found on:
# http://wordlist.sourceforge.net/12dicts-readme.html
def getWords(letters):

    result = []
    wordsAlreadyPrinted = set()
    permutations = itertools.permutations(letters)
    
    for permutation in permutations:
        
        curWord = ""
        
        for char in permutation:
            curWord += char
            
        if curWord in allWords and not curWord in wordsAlreadyPrinted:
            result.append(curWord)
            wordsAlreadyPrinted.add(curWord)

    return result

# The main loop
def main():
    # Initialize the set of known words
    init()

    # Request new queries until a blank line is submitted
    while True:
                          
        print("Enter a word to unscramble (ENTER to quit): ", end = "")
        letters = input()
        
        if letters == "":
            break

        print("\nWorking...", end = "")
        result = getWords(letters)
        
        print("\nThe following words may be created from " + letters + ":\n")
        
        if result != []:
            for s in result:
                print(s)
        else:
            print("(no results)")

        print()

main()
