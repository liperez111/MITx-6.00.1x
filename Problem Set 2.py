def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    nwords = len(secretWord)
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(nwords) + " letters long.")
    print("-----------")

    mistakesMade = 0


    while isWordGuessed(secretWord, lettersGuessed) == False:
        if mistakesMade < 8:
            print("You have " + str(8 - mistakesMade) + " guesses left.")
            print("Available letters: " + getAvailableLetters(lettersGuessed))

            guess = input("Please guess a letter: ")
            guessInLowerCase = guess.lower()


            if guessInLowerCase in lettersGuessed:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print("-----------")
            else:
                if guessInLowerCase in secretWord:
                    lettersGuessed.append(guessInLowerCase)
                    print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                    print("-----------")
                else:
                    lettersGuessed.append(guessInLowerCase)
                    print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                    print("-----------")
                    mistakesMade += 1
        else:
            print("Sorry, you ran out of guesses. The word was " + secretWord)
            break
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print("Congratulations, you won!")