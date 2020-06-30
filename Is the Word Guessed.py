def isWordGuessed(secretWord, lettersGuessed):
    n = 0
    for i in lettersGuessed:
        if i in secretWord:
            n += 1
            if n == len(secretWord):
                return True
                break




secretWord = 'aple'
lettersGuessed = ['e', 'i', 'k', 'p','a','r','l', 's']

print(isWordGuessed(secretWord,lettersGuessed))
