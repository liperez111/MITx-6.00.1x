from ps4a import *
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    handel = hand.copy()
    if word == "":
        return False
    elif word in wordList:
        for i in word:
            if i not in handel or handel[i] == 0:
                return False
            else:
                handel[i] -= 1
        return True
    else:
        return False

wordList = loadWords()

print(isValidWord("tasf",{'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1},wordList))
