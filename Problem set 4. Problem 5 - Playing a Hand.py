from ps4a import *

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
n = HAND_SIZE

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4}
WORDLIST_FILENAME = "words.txt"


def playHand(hand, wordList, n):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """

    # Keep track of the total
    totalscore = 0

    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
    # Display the hand
       
        print("Current Hand:",end=" " ); displayHand(hand)

    # Ask user for input
        word = str(input('Enter word, or a "." to indicate that you are finished: '))

    # If the input is a single period:
        if word == ".":

    # End the game (break out of the loop)
            break
    # Otherwise (the input is not a single period):
        else:
    # If the word is not valid:
            if isValidWord(word,hand,wordList) == False:

    # Reject invalid word (print a message followed by a blank line)
                print('Invalid word, please try again.', '\n')
    # Otherwise (the word is valid):
            else:
    # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                totalscore += getWordScore(word, n)
                print('"' + word + '"', "earned", getWordScore(word, n), "points. Total:", totalscore, "points", '\n')

    # Update the hand
                hand = updateHand(hand,word)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if word == '.':
        print('Goodbye! Total score:', totalscore, 'points.')
    else:
        print('Run out of letters. Total score:', totalscore, 'points.')


wordList = loadWords()
playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)
