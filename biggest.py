

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: The key with the largest number of values associated with it
    '''
    biggest = 0
    collection = []
    # Your Code Here
    if len(aDict) == 0:
        return None
    for e in aDict:
        if len(aDict[e]) >= biggest:
            biggest = len(aDict[e])
            collection = e


    return str(collection)

print(biggest(animals))