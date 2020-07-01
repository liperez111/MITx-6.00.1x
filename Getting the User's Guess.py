def isWordGuessed(secretWord, lettersGuessed):

    word = []
    for i in secretWord:
        if i in lettersGuessed:

            word.append(i)
        else:
            word.append("_")

    w = ' '.join(word)
    return w





secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

print(isWordGuessed(secretWord, lettersGuessed))
