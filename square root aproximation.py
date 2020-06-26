#square root aproximation


def square(y):
    epsilon = 0.0000000001
    guess = y/2.0
    numGuesses = 0

    while abs(guess*guess - y) >= epsilon:
        numGuesses += 1
        guess = guess - (((guess**2)-y)/(2*guess))

    return guess


print(square(100))
