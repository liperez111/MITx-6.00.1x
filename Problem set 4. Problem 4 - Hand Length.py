def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    suma = 0
    for i in hand:
        suma += hand[i]
    return suma

print(calculateHandlen({'h': 1, 'e': 1, 'l': 2, 'o': 1}))