def isWordGuessed(secretWord, lettersGuessed):
    n = 0

    for i in secretWord:
        if i in lettersGuessed:
            n += 1
            if n == len(secretWord):
                return True
                break
        elif n != len(secretWord):
            return False



secretWord = 'durian'
lettersGuessed = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']

print(isWordGuessed(secretWord,lettersGuessed))
