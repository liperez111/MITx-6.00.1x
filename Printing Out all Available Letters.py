def getAvailableLetters(lettersGuessed):
    avl = []
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in lettersGuessed:
            avl.append(i)

    al = "".join(avl)
    return al


lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

print(getAvailableLetters(lettersGuessed))